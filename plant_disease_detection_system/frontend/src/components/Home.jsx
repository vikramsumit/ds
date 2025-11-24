import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 to-blue-50">
      <div className="container mx-auto px-4 py-16">
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold text-gray-800 mb-6">
            🌱 Plant Disease Detection
          </h1>
          <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
            Upload or capture an image of your plant to identify diseases and get treatment recommendations.
            Our AI-powered system supports 9 different plant types with comprehensive disease detection.
          </p>
          <Link
            to="/capture"
            className="inline-block bg-green-600 text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-green-700 transition-colors shadow-lg"
          >
            Start Detection
          </Link>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
          <div className="bg-white p-6 rounded-lg shadow-md">
            <div className="text-4xl mb-4">📷</div>
            <h3 className="text-xl font-semibold mb-2">Easy Capture</h3>
            <p className="text-gray-600">
              Use your camera or upload existing photos for instant analysis.
            </p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-md">
            <div className="text-4xl mb-4">🤖</div>
            <h3 className="text-xl font-semibold mb-2">AI-Powered</h3>
            <p className="text-gray-600">
              Advanced machine learning identifies plants and diseases with high accuracy.
            </p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-md">
            <div className="text-4xl mb-4">💊</div>
            <h3 className="text-xl font-semibold mb-2">Treatment Guide</h3>
            <p className="text-gray-600">
              Get detailed information about diseases and recommended treatments.
            </p>
          </div>
        </div>

        <div className="bg-white p-8 rounded-lg shadow-md">
          <h2 className="text-3xl font-bold text-center mb-8">Supported Plants</h2>
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
            {[
              'Apple', 'Bell Pepper', 'Cherry', 'Corn (Maize)',
              'Grape', 'Peach', 'Potato', 'Strawberry', 'Tomato'
            ].map((plant) => (
              <div key={plant} className="text-center p-4 bg-green-50 rounded-lg">
                <div className="text-2xl mb-2">🌿</div>
                <p className="font-medium">{plant}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
