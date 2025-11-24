const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white py-8">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 className="text-lg font-semibold mb-4">🌱 Plant Disease Detector</h3>
            <p className="text-gray-300">
              Advanced AI-powered plant disease detection to help farmers and gardeners identify and treat plant diseases early.
            </p>
          </div>
          <div>
            <h3 className="text-lg font-semibold mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li><a href="/" className="text-gray-300 hover:text-white">Home</a></li>
              <li><a href="/about" className="text-gray-300 hover:text-white">About</a></li>
              <li><a href="/contribute" className="text-gray-300 hover:text-white">Contribute</a></li>
            </ul>
          </div>
          <div>
            <h3 className="text-lg font-semibold mb-4">Contact Me</h3>
            <p className="text-gray-300">
              Have questions or feedback? Reach out to us for support and improvements.
            </p>
          </div>
        </div>
        <div className="border-t border-gray-400 mt-8 pt-8 text-center">
          <p className="text-gray-300">
            © 2024-{new Date().getFullYear()} Plant Disease Detection
          </p>
          <p className="text-gray-300 mt-3">
            System Built with ❤️ for sustainable agriculture.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
