import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './components/Home';
import Capture from './components/Capture';
import Preview from './components/Preview';
import Results from './components/Results';

function App() {
  return (
    <Router>
      <div className="min-h-screen flex flex-col">
        <Navbar />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/capture" element={<Capture />} />
            <Route path="/preview" element={<Preview />} />
            <Route path="/results" element={<Results />} />
            <Route path="/about" element={
              <div className="min-h-screen bg-gray-50 py-16">
                <div className="container mx-auto px-4 max-w-4xl">
                  <h1 className="text-4xl font-bold text-center mb-8">About Plant Disease Detector</h1>
                  <div className="bg-white p-8 rounded-lg shadow-md">
                    <p className="text-lg text-gray-700 mb-6">
                      This advanced plant disease detection system uses artificial intelligence and machine learning
                      to help farmers and gardeners identify plant diseases quickly and accurately.
                    </p>
                    <p className="text-gray-700 mb-6">
                      Our system supports 9 different plant types and can detect various diseases affecting crops,
                      helping to prevent yield losses and improve agricultural productivity.
                    </p>
                    <h2 className="text-2xl font-semibold mb-4">Features:</h2>
                    <ul className="list-disc list-inside text-gray-700 space-y-2">
                      <li>Real-time image capture and analysis</li>
                      <li>Support for multiple plant species</li>
                      <li>Detailed disease information and treatment recommendations</li>
                      <li>User-friendly web interface</li>
                      <li>High accuracy AI-powered predictions</li>
                    </ul>
                  </div>
                </div>
              </div>
            } />
            <Route path="/contribute" element={
              <div className="min-h-screen bg-gray-50 py-16">
                <div className="container mx-auto px-4 max-w-4xl">
                  <h1 className="text-4xl font-bold text-center mb-8">Contribute</h1>
                  <div className="bg-white p-8 rounded-lg shadow-md">
                    <p className="text-lg text-gray-700 mb-6">
                      Help us improve the Plant Disease Detection System by contributing your expertise and resources.
                    </p>
                    <h2 className="text-2xl font-semibold mb-4">Ways to Contribute:</h2>
                    <ul className="list-disc list-inside text-gray-700 space-y-2">
                      <li>Report bugs and suggest improvements</li>
                      <li>Contribute to the codebase on GitHub</li>
                      <li>Help expand support for more plant species</li>
                      <li>Provide feedback on accuracy and usability</li>
                      <li>Share the project with others in the agricultural community</li>
                    </ul>
                    <div className="mt-8">
                      <a
                        href="https://github.com"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-block bg-gray-800 text-white px-6 py-3 rounded-lg hover:bg-gray-900 transition-colors"
                      >
                        View on GitHub
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            } />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
