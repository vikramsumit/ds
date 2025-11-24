import { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';

const Capture = () => {
  const [image, setImage] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [isCameraActive, setIsCameraActive] = useState(false);
  const [error, setError] = useState('');
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const fileInputRef = useRef(null);
  const navigate = useNavigate();

  const startCamera = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      videoRef.current.srcObject = stream;
      setIsCameraActive(true);
      setError('');
    } catch (err) {
      setError('Camera access denied or not available');
      console.error('Error accessing camera:', err);
    }
  };

  const stopCamera = () => {
    if (videoRef.current && videoRef.current.srcObject) {
      const stream = videoRef.current.srcObject;
      const tracks = stream.getTracks();
      tracks.forEach(track => track.stop());
      videoRef.current.srcObject = null;
    }
    setIsCameraActive(false);
  };

  const captureImage = () => {
    if (!videoRef.current || !canvasRef.current) return;

    const canvas = canvasRef.current;
    const video = videoRef.current;
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0);

    canvas.toBlob((blob) => {
      const file = new File([blob], 'captured-image.jpg', { type: 'image/jpeg' });
      setImage(file);
      setImagePreview(URL.createObjectURL(blob));
      stopCamera();
    }, 'image/jpeg');
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      if (!file.type.startsWith('image/')) {
        setError('Please select a valid image file');
        return;
      }
      if (file.size > 5 * 1024 * 1024) { // 5MB limit
        setError('File size must be less than 5MB');
        return;
      }
      setImage(file);
      setImagePreview(URL.createObjectURL(file));
      setError('');
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleDrop = (e) => {
    e.preventDefault();
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      const file = files[0];
      if (file.type.startsWith('image/')) {
        if (file.size > 5 * 1024 * 1024) {
          setError('File size must be less than 5MB');
          return;
        }
        setImage(file);
        setImagePreview(URL.createObjectURL(file));
        setError('');
      } else {
        setError('Please drop a valid image file');
      }
    }
  };

  const proceedToPreview = () => {
    if (image) {
      navigate('/preview', { state: { image, imagePreview } });
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container mx-auto px-4 max-w-4xl">
        <h1 className="text-3xl font-bold text-center mb-8">Capture Plant Image</h1>

        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
            {error}
          </div>
        )}

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Camera/File Upload Section */}
          <div className="space-y-6">
            {/* Camera Controls */}
            <div className="bg-white p-6 rounded-lg shadow-md">
              <h2 className="text-xl font-semibold mb-4">📷 Camera Capture</h2>
              <div className="space-y-4">
                {!isCameraActive ? (
                  <button
                    onClick={startCamera}
                    className="w-full bg-blue-600 text-white py-3 px-4 rounded-lg hover:bg-blue-700 transition-colors"
                  >
                    Start Camera
                  </button>
                ) : (
                  <div className="space-y-4">
                    <video
                      ref={videoRef}
                      autoPlay
                      className="w-full rounded-lg border"
                    />
                    <div className="flex space-x-4">
                      <button
                        onClick={captureImage}
                        className="flex-1 bg-green-600 text-white py-2 px-4 rounded-lg hover:bg-green-700 transition-colors"
                      >
                        Capture
                      </button>
                      <button
                        onClick={stopCamera}
                        className="flex-1 bg-red-600 text-white py-2 px-4 rounded-lg hover:bg-red-700 transition-colors"
                      >
                        Stop Camera
                      </button>
                    </div>
                  </div>
                )}
              </div>
            </div>

            {/* File Upload */}
            <div className="bg-white p-6 rounded-lg shadow-md">
              <h2 className="text-xl font-semibold mb-4">📁 Upload Image</h2>
              <div
                className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center hover:border-gray-400 transition-colors cursor-pointer"
                onDragOver={handleDragOver}
                onDrop={handleDrop}
                onClick={() => fileInputRef.current.click()}
              >
                <div className="text-4xl mb-4">📤</div>
                <p className="text-gray-600 mb-2">
                  Drag & drop an image here, or click to select
                </p>
                <p className="text-sm text-gray-500">
                  Supports JPG, PNG, WebP (max 5MB)
                </p>
                <input
                  ref={fileInputRef}
                  type="file"
                  accept="image/*"
                  onChange={handleFileUpload}
                  className="hidden"
                />
              </div>
            </div>
          </div>

          {/* Preview Section */}
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-xl font-semibold mb-4">🖼️ Preview</h2>
            <div className="aspect-square bg-gray-100 rounded-lg flex items-center justify-center mb-4">
              {imagePreview ? (
                <img
                  src={imagePreview}
                  alt="Preview"
                  className="max-w-full max-h-full rounded-lg"
                />
              ) : (
                <div className="text-gray-400 text-center">
                  <div className="text-4xl mb-2">📷</div>
                  <p>No image selected</p>
                </div>
              )}
            </div>
            {image && (
              <div className="text-sm text-gray-600 mb-4">
                <p><strong>File:</strong> {image.name}</p>
                <p><strong>Size:</strong> {(image.size / 1024 / 1024).toFixed(2)} MB</p>
              </div>
            )}
            <button
              onClick={proceedToPreview}
              disabled={!image}
              className={`w-full py-3 px-4 rounded-lg transition-colors ${
                image
                  ? 'bg-green-600 text-white hover:bg-green-700'
                  : 'bg-gray-300 text-gray-500 cursor-not-allowed'
              }`}
            >
              Proceed to Analysis
            </button>
          </div>
        </div>

        {/* Hidden canvas for capture */}
        <canvas ref={canvasRef} className="hidden" />
      </div>
    </div>
  );
};

export default Capture;
