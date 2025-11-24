const express = require('express');
const multer = require('multer');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Configure multer for file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const tempDir = path.join(__dirname, '../temp');
    if (!fs.existsSync(tempDir)) {
      fs.mkdirSync(tempDir, { recursive: true });
    }
    cb(null, tempDir);
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + path.extname(file.originalname));
  }
});

const upload = multer({
  storage: storage,
  fileFilter: (req, file, cb) => {
    if (file.mimetype.startsWith('image/')) {
      cb(null, true);
    } else {
      cb(new Error('Only image files are allowed!'), false);
    }
  },
  limits: {
    fileSize: 5 * 1024 * 1024 // 5MB limit
  }
});

// Load diseases data
let diseasesData;
try {
  diseasesData = JSON.parse(fs.readFileSync(path.join(__dirname, '../diseases.json'), 'utf8'));
} catch (error) {
  console.error('Error loading diseases.json:', error);
  diseasesData = {};
}

// API Routes
app.get('/api/disease', (req, res) => {
  res.json(diseasesData);
});

app.post('/api/predict', upload.single('image'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No image file provided' });
  }

  const imagePath = req.file.path;

  // Spawn Python process
  const pythonProcess = spawn('python3', ['../combined_predict.py', imagePath], {
    cwd: __dirname,
    stdio: ['pipe', 'pipe', 'pipe']
  });

  let output = '';
  let errorOutput = '';

  pythonProcess.stdout.on('data', (data) => {
    output += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    errorOutput += data.toString();
  });

  pythonProcess.on('close', (code) => {
    // Clean up temp file
    fs.unlink(imagePath, (err) => {
      if (err) console.error('Error deleting temp file:', err);
    });

    if (code !== 0) {
      console.error('Python script error:', errorOutput);
      return res.status(500).json({ error: 'Prediction failed', details: errorOutput });
    }

    try {
      // Parse the output - the script prints the result dict
      const lines = output.trim().split('\n');
      const resultLine = lines.find(line => line.includes('Final Result:'));
      if (!resultLine) {
        return res.status(500).json({ error: 'Could not parse prediction result' });
      }

      // Extract plant and disease from the output
      const plantMatch = output.match(/Plant: ([^(]+) \(([^)]+)\)/);
      const diseaseMatch = output.match(/Disease: ([^(]+) \(([^)]+)\)/);

      if (!plantMatch || !diseaseMatch) {
        return res.status(500).json({ error: 'Could not parse prediction details' });
      }

      const result = {
        plant: plantMatch[1].trim(),
        plant_confidence: parseFloat(plantMatch[2]),
        disease: diseaseMatch[1].trim(),
        disease_confidence: parseFloat(diseaseMatch[2])
      };

      res.json(result);
    } catch (parseError) {
      console.error('Parse error:', parseError);
      res.status(500).json({ error: 'Failed to parse prediction result', details: output });
    }
  });

  pythonProcess.on('error', (error) => {
    console.error('Process error:', error);
    fs.unlink(imagePath, (err) => {
      if (err) console.error('Error deleting temp file:', err);
    });
    res.status(500).json({ error: 'Prediction process failed' });
  });
});

// Error handling middleware
app.use((error, req, res, next) => {
  if (error instanceof multer.MulterError) {
    if (error.code === 'LIMIT_FILE_SIZE') {
      return res.status(400).json({ error: 'File too large. Maximum size is 5MB.' });
    }
  }
  res.status(500).json({ error: error.message });
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on port ${PORT}`);
});
