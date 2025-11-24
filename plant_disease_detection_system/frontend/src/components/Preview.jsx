import { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

const Preview = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { image, imagePreview } = location.state || {};
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [error, setError] = useState('');

  if (!image || !imagePreview) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-gray-800 mb-4">No Image Found</h1>
          <button
            onClick={() => navigate('/capture')}
            className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700"
          >
            Go Back to Capture
          </button>
        </div>
      </div>
    );
  }

  const analyzeImage = async () => {
    setIsAnalyzing(true);
    setError('');

    try {
      const formData = new FormData();
      formData.append('image', image);

      const response = await fetch('/api/predict', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Analysis failed');
      }

      const result = await response.json();
      navigate('/results', { state: { result, imagePreview } });
    } catch (err) {
      setError(err.message);
      console.error('Analysis error:', err);
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container mx-auto px-4 max-w-2xl">
        <h1 className="text-3xl font-bold text-center mb-8">Confirm Image</h1>

        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
            {error}
          </div>
        )}

        <div className="bg-white p-6 rounded-lg shadow-md">
          <div className="mb-6">
            <h2 className="text-xl font-semibold mb-4">📷 Selected Image</h2>
            <div className="aspect-square bg-gray-100 rounded-lg overflow-hidden">
              <img
                src={imagePreview}
                alt="Selected plant"
                className="w-full h-full object-cover"
              />
            </div>
          </div>

          <div className="text-sm text-gray-600 mb-6">
            <p><strong>File:</strong> {image.name}</p>
            <p><strong>Size:</strong> {(image.size / 1024 / 1024).toFixed(2)} MB</p>
          </div>

          <div className="flex space-x-4">
            <button
              onClick={() => navigate('/capture')}
              className="flex-1 bg-gray-600 text-white py-3 px-4 rounded-lg hover:bg-gray-700 transition-colors"
              disabled={isAnalyzing}
            >
              Retake/Change
            </button>
            <button
              onClick={analyzeImage}
              disabled={isAnalyzing}
              className={`flex-1 py-3 px-4 rounded-lg transition-colors ${
                isAnalyzing
                  ? 'bg-gray-400 text-gray-700 cursor-not-allowed'
                  : 'bg-green-600 text-white hover:bg-green-700'
              }`}
            >
              {isAnalyzing ? (
                <div className="flex items-center justify-center">
                  <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                  Analyzing...
                </div>
              ) : (
                'Analyze Plant'
              )}
            </button>
          </div>
        </div>

        <div className="mt-8 text-center">
          <p className="text-gray-600">
            Our AI will analyze the image to identify the plant type and detect any diseases.
            This may take a few seconds.
          </p>
        </div>
      </div>
    </div>
  );
};

export default Preview;
