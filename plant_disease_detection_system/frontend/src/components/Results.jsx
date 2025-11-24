// import { useState, useEffect } from 'react';
// import { useLocation, useNavigate } from 'react-router-dom';

// const Results = () => {
//   const location = useLocation();
//   const navigate = useNavigate();
//   const { result, imagePreview } = location.state || {};
//   const [diseaseInfo, setDiseaseInfo] = useState(null);
//   const [loadingDisease, setLoadingDisease] = useState(false);

//   if (!result || !imagePreview) {
//     return (
//       <div className="min-h-screen bg-gray-50 flex items-center justify-center">
//         <div className="text-center">
//           <h1 className="text-2xl font-bold text-gray-800 mb-4">No Results Found</h1>
//           <button
//             onClick={() => navigate('/capture')}
//             className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700"
//           >
//             Start New Analysis
//           </button>
//         </div>
//       </div>
//     );
//   }

//   useEffect(() => {
//     const fetchDiseaseInfo = async () => {
//       setLoadingDisease(true);
//       try {
//         const response = await fetch('/api/disease');
//         if (response.ok) {
//           const diseases = await response.json();
//           const key = `${result.plant}_${result.disease}`;
//           setDiseaseInfo(diseases[key] || null);
//         }
//       } catch (error) {
//         console.error('Error fetching disease info:', error);
//       } finally {
//         setLoadingDisease(false);
//       }
//     };

//     fetchDiseaseInfo();
//   }, [result]);

//   const getConfidenceColor = (confidence) => {
//     if (confidence >= 90) return 'text-green-600';
//     if (confidence >= 70) return 'text-yellow-600';
//     return 'text-red-600';
//   };

//   const getConfidenceBg = (confidence) => {
//     if (confidence >= 90) return 'bg-green-100';
//     if (confidence >= 70) return 'bg-yellow-100';
//     return 'bg-red-100';
//   };

//   return (
//     <div className="min-h-screen bg-gray-50 py-8">
//       <div className="container mx-auto px-4 max-w-4xl">
//         <h1 className="text-3xl font-bold text-center mb-8">Analysis Results</h1>

//         <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
//           {/* Image Preview */}
//           <div className="bg-white p-6 rounded-lg shadow-md">
//             <h2 className="text-xl font-semibold mb-4">📷 Analyzed Image</h2>
//             <div className="aspect-square bg-gray-100 rounded-lg overflow-hidden">
//               <img
//                 src={imagePreview}
//                 alt="Analyzed plant"
//                 className="w-full h-full object-cover"
//               />
//             </div>
//           </div>

//           {/* Prediction Results */}
//           <div className="bg-white p-6 rounded-lg shadow-md">
//             <h2 className="text-xl font-semibold mb-4">🔍 Prediction Results</h2>

//             <div className="space-y-4">
//               <div className={`p-4 rounded-lg ${getConfidenceBg(result.plant_confidence)}`}>
//                 <div className="flex justify-between items-center mb-2">
//                   <span className="font-medium">Leaf Type/ Plant of:</span>
//                   <span className={`font-bold ${getConfidenceColor(result.plant_confidence)}`}>
//                     {result.plant_confidence.toFixed(1)}%
//                   </span>
//                 </div>
//                 <p className="text-lg font-semibold">{result.plant}</p>
//               </div>

//               <div className={`p-4 rounded-lg ${getConfidenceBg(result.disease_confidence)}`}>
//                 <div className="flex justify-between items-center mb-2">
//                   <span className="font-medium">Disease Status:</span>
//                   <span className={`font-bold ${getConfidenceColor(result.disease_confidence)}`}>
//                     {result.disease_confidence.toFixed(1)}%
//                   </span>
//                 </div>
//                 <p className="text-lg font-semibold">{result.disease}</p>
//               </div>

//               {result.plant_confidence < 50 && (
//                 <div className="bg-yellow-100 border border-yellow-400 text-yellow-800 px-4 py-3 rounded">
//                   <strong>Low Confidence:</strong> The plant identification confidence is below 50%.
//                   Consider retaking the photo with better lighting and focus.
//                 </div>
//               )}
//             </div>
//           </div>
//         </div>

//         {/* Disease Information */}
//         {diseaseInfo && (
//           <div className="mt-8 bg-white p-6 rounded-lg shadow-md">
//             <h2 className="text-2xl font-semibold mb-6">💊 Disease Information</h2>

//             <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
//               <div>
//                 <h3 className="text-lg font-semibold text-red-600 mb-2">📋 Summary</h3>
//                 <p className="text-gray-700">{diseaseInfo.summary}</p>
//               </div>

//               <div>
//                 <h3 className="text-lg font-semibold text-blue-600 mb-2">💉 Treatment</h3>
//                 <p className="text-gray-700">{diseaseInfo.cure}</p>
//               </div>

//               <div>
//                 <h3 className="text-lg font-semibold text-green-600 mb-2">🛡️ Prevention</h3>
//                 <p className="text-gray-700">{diseaseInfo.prevention}</p>
//               </div>
//             </div>
//           </div>
//         )}

//         {loadingDisease && (
//           <div className="mt-8 bg-white p-6 rounded-lg shadow-md">
//             <div className="flex items-center justify-center">
//               <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-green-600 mr-4"></div>
//               <p>Loading disease information...</p>
//             </div>
//           </div>
//         )}

//         {!diseaseInfo && !loadingDisease && result.disease !== 'Healthy' && (
//           <div className="mt-8 bg-gray-100 p-6 rounded-lg">
//             <p className="text-gray-600">
//               Disease information not available for this specific case.
//             </p>
//           </div>
//         )}

//         {/* Action Buttons */}
//         <div className="mt-8 text-center space-x-4">
//           <button
//             onClick={() => navigate('/capture')}
//             className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors"
//           >
//             Analyze Another Plant
//           </button>
//           <button
//             onClick={() => navigate('/')}
//             className="bg-gray-600 text-white px-6 py-3 rounded-lg hover:bg-gray-700 transition-colors"
//           >
//             Back to Home
//           </button>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default Results;

import { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

export default function Results() {
  const location = useLocation();
  const navigate = useNavigate();
  const { result, imagePreview } = location.state || {};

  const [diseaseInfo, setDiseaseInfo] = useState(null);
  const [loadingDisease, setLoadingDisease] = useState(false);
  const [error, setError] = useState(null);

  // Return early if required data is missing (defensive)
  if (!result || !imagePreview) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center px-6">
          <h1 className="text-2xl font-bold text-gray-800 mb-4">No Results Found</h1>
          <p className="text-gray-600 mb-6">Please capture an image first to see analysis results.</p>
          <div className="flex justify-center gap-4">
            <button
              onClick={() => navigate('/capture')}
              className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-300"
            >
              Start New Analysis
            </button>
            <button
              onClick={() => navigate('/')}
              className="bg-gray-600 text-white px-6 py-3 rounded-lg hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-300"
            >
              Back to Home
            </button>
          </div>
        </div>
      </div>
    );
  }

  // Normalise confidence values: support both 0-1 and 0-100 scales
  const normalizeConfidence = (val) => {
    if (val == null || Number.isNaN(Number(val))) return 0;
    const n = Number(val);
    return n <= 1 ? n * 100 : n;
  };

  const plantConfidence = normalizeConfidence(result.plant_confidence);
  const diseaseConfidence = normalizeConfidence(result.disease_confidence);

  useEffect(() => {
    let mounted = true;
    const controller = new AbortController();

    const fetchDiseaseInfo = async () => {
      setLoadingDisease(true);
      setError(null);
      try {
        const resp = await fetch('/api/disease', { signal: controller.signal });
        if (!resp.ok) {
          throw new Error(`Server returned ${resp.status}`);
        }

        const diseases = await resp.json();

        // Try a few key variants to match dataset keys (space vs underscore, case variations)
        const rawKey = `${result.plant}_${result.disease}`;
        const variants = [
          rawKey,
          rawKey.replace(/\s+/g, '_'),
          rawKey.replace(/\s+/g, '_').toLowerCase(),
          rawKey.replace(/\s+/g, '').toLowerCase(),
        ];

        let info = null;
        for (const k of variants) {
          if (Object.prototype.hasOwnProperty.call(diseases, k)) {
            info = diseases[k];
            break;
          }
        }

        // If mounted, set state
        if (mounted) setDiseaseInfo(info || null);
      } catch (err) {
        if (err.name === 'AbortError') return; // ignore abort
        console.error('Error fetching disease info:', err);
        if (mounted) setError(err.message || 'Failed to load disease info');
      } finally {
        if (mounted) setLoadingDisease(false);
      }
    };

    fetchDiseaseInfo();

    return () => {
      mounted = false;
      controller.abort();
    };
  }, [result]);

  const getConfidenceColor = (confidence) => {
    if (confidence >= 90) return 'text-green-600';
    if (confidence >= 70) return 'text-yellow-600';
    return 'text-red-600';
  };

  const getConfidenceBg = (confidence) => {
    if (confidence >= 90) return 'bg-green-100';
    if (confidence >= 70) return 'bg-yellow-100';
    return 'bg-red-100';
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container mx-auto px-4 max-w-4xl">
        <h1 className="text-3xl font-bold text-center mb-8">Analysis Results</h1>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Image Preview */}
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-xl font-semibold mb-4">📷 Analyzed Image</h2>
            <div className="aspect-square bg-gray-100 rounded-lg overflow-hidden">
              <img
                src={imagePreview}
                alt={`Analyzed ${result.plant} example`}
                className="w-full h-full object-cover"
                loading="lazy"
              />
            </div>
          </div>

          {/* Prediction Results */}
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-xl font-semibold mb-4">🔍 Prediction Results</h2>

            <div className="space-y-4">
              <div className={`p-4 rounded-lg ${getConfidenceBg(plantConfidence)}`}>
                <div className="flex justify-between items-center mb-2">
                  <span className="font-medium">Leaf Type / Plant:</span>
                  <span className={`font-bold ${getConfidenceColor(plantConfidence)}`}>
                    {plantConfidence.toFixed(1)}%
                  </span>
                </div>
                <p className="text-lg font-semibold break-words">{result.plant}</p>
              </div>

              <div className={`p-4 rounded-lg ${getConfidenceBg(diseaseConfidence)}`}>
                <div className="flex justify-between items-center mb-2">
                  <span className="font-medium">Disease Status:</span>
                  <span className={`font-bold ${getConfidenceColor(diseaseConfidence)}`}>
                    {diseaseConfidence.toFixed(1)}%
                  </span>
                </div>
                <p className="text-lg font-semibold break-words">{result.disease}</p>
              </div>

              {plantConfidence < 50 && (
                <div className="bg-yellow-50 border border-yellow-400 text-yellow-800 px-4 py-3 rounded">
                  <strong>Low Confidence:</strong> The plant identification confidence is below 50%.
                  Consider retaking the photo with better lighting, from a closer/focused angle, and avoid cluttered backgrounds.
                </div>
              )}
            </div>

            {/* Optional small note about confidence */}
            <p className="mt-4 text-sm text-gray-500">Confidences are normalized to a 0–100% scale for display.</p>
          </div>
        </div>

        {/* Disease Information */}
        {loadingDisease && (
          <div className="mt-8 bg-white p-6 rounded-lg shadow-md">
            <div className="flex items-center justify-center">
              <div className="animate-spin rounded-full h-8 w-8 border-4 border-b-2 border-green-600 mr-4" aria-hidden></div>
              <p>Loading disease information...</p>
            </div>
          </div>
        )}

        {error && (
          <div className="mt-8 bg-red-50 border border-red-200 p-6 rounded-lg text-red-700">
            <strong>Error:</strong> {error}
          </div>
        )}

        {diseaseInfo && !loadingDisease && (
          <div className="mt-8 bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-2xl font-semibold mb-6">💊 Disease Information</h2>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div>
                <h3 className="text-lg font-semibold text-red-600 mb-2">📋 Summary</h3>
                <p className="text-gray-700">{diseaseInfo.summary}</p>
              </div>

              <div>
                <h3 className="text-lg font-semibold text-blue-600 mb-2">💉 Treatment</h3>
                <p className="text-gray-700">{diseaseInfo.cure}</p>
              </div>

              <div>
                <h3 className="text-lg font-semibold text-green-600 mb-2">🛡️ Prevention</h3>
                <p className="text-gray-700">{diseaseInfo.prevention}</p>
              </div>
            </div>

            {/* Optional: list monitoring / notes if present */}
            {diseaseInfo.monitoring && (
              <div className="mt-6">
                <h4 className="font-semibold">Monitoring / Notes</h4>
                <p className="text-gray-700">{diseaseInfo.monitoring}</p>
              </div>
            )}
          </div>
        )}

        {!diseaseInfo && !loadingDisease && !error && result.disease !== 'Healthy' && (
          <div className="mt-8 bg-gray-100 p-6 rounded-lg">
            <p className="text-gray-600">Disease information not available for this specific case.</p>
          </div>
        )}

        {/* Action Buttons */}
        <div className="mt-8 text-center space-x-4">
          <button
            onClick={() => navigate('/capture')}
            className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors focus:outline-none focus:ring-2 focus:ring-blue-300"
          >
            Analyze Another Plant
          </button>
          <button
            onClick={() => navigate('/')}
            className="bg-gray-600 text-white px-6 py-3 rounded-lg hover:bg-gray-700 transition-colors focus:outline-none focus:ring-2 focus:ring-gray-300"
          >
            Back to Home
          </button>
        </div>
      </div>
    </div>
  );
}
