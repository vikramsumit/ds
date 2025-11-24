// Navbar.jsx
import { Link, useLocation } from 'react-router-dom';
import { useEffect, useState } from 'react';

const Navbar = () => {
  const location = useLocation();
  const [open, setOpen] = useState(false);

  // Close the menu on route change
  useEffect(() => {
    setOpen(false);
  }, [location.pathname]);

  // Lock body scroll when the mobile menu is open
  useEffect(() => {
    if (open) document.body.classList.add('overflow-hidden');
    else document.body.classList.remove('overflow-hidden');
    return () => document.body.classList.remove('overflow-hidden');
  }, [open]);

  // Close on Escape
  useEffect(() => {
    const onKey = (e) => e.key === 'Escape' && setOpen(false);
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, []);

  const isActive = (path) =>
    location.pathname === path || (path !== '/' && location.pathname.startsWith(path));

  const navLink =
    'block px-3 py-2 rounded-md transition hover:text-green-200 focus:outline-none focus:ring-2 focus:ring-white/60';

  return (
    <nav className="sticky top-0 z-50 bg-green-600 text-white shadow-lg">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          {/* Logo / Brand */}
          <Link
            to="/"
            className="flex items-center gap-2 text-lg sm:text-2xl font-bold hover:text-green-200 focus:outline-none focus:ring-2 focus:ring-white/60 rounded-md"
          >
            <span role="img" aria-label="seedling">🌱</span>
            <span className="hidden xs:inline">Plant Disease Detection System</span>
            <span className="xs:hidden">Plant Disease Detection System</span>
          </Link>

          {/* Desktop nav */}
          <nav className="hidden md:flex items-center gap-1">
            <Link
              to="/"
              className={`${navLink} ${isActive('/') ? 'font-semibold underline underline-offset-4' : ''}`}
              aria-current={isActive('/') ? 'page' : undefined}
            >
              Home
            </Link>
            <Link
              to="/about"
              className={`${navLink} ${isActive('/about') ? 'font-semibold underline underline-offset-4' : ''}`}
              aria-current={isActive('/about') ? 'page' : undefined}
            >
              About
            </Link>
            <Link
              to="/contact"
              className={`${navLink} ${isActive('/contact') ? 'font-semibold underline underline-offset-4' : ''}`}
              aria-current={isActive('/contact') ? 'page' : undefined}
            >
              Contact Us
            </Link>
            <Link
              to="/contribute"
              className={`${navLink} ${isActive('/contribute') ? 'font-semibold underline underline-offset-4' : ''}`}
              aria-current={isActive('/contribute') ? 'page' : undefined}
            >
              Contribute
            </Link>
          </nav>

          {/* Mobile hamburger */}
          <button
            type="button"
            className="md:hidden inline-flex items-center justify-center rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-white/60"
            aria-controls="mobile-menu"
            aria-expanded={open}
            onClick={() => setOpen((v) => !v)}
          >
            <span className="sr-only">Toggle main menu</span>
            {open ? (
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" viewBox="0 0 24 24" fill="none"
                stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <line x1="18" y1="6" x2="6" y2="18" />
                <line x1="6" y1="6" x2="18" y2="18" />
              </svg>
            ) : (
              <svg xmlns="http://www.w3.org/2000/svg" className="h-7 w-7" viewBox="0 0 24 24" fill="none"
                stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <line x1="3" y1="6" x2="21" y2="6" />
                <line x1="3" y1="12" x2="21" y2="12" />
                <line x1="3" y1="18" x2="21" y2="18" />
              </svg>
            )}
          </button>
        </div>
      </div>

      {/* Mobile menu panel - KEEP IN DOM, control with classes */}
      <div
        id="mobile-menu"
        className={`md:hidden overflow-hidden transition-all duration-300 ease-in-out ${
          open ? 'max-h-96 opacity-100' : 'max-h-0 opacity-0'
        }`}
        aria-hidden={!open}
      >
        <nav className="bg-green-700/95 backdrop-blur px-4 pt-2 pb-4 shadow-md rounded-b-2xl">
          <Link
            to="/"
            className={`${navLink} ${isActive('/') ? 'font-semibold underline underline-offset-4' : ''}`}
            aria-current={isActive('/') ? 'page' : undefined}
          >
            Home
          </Link>
          <Link
            to="/about"
            className={`${navLink} ${isActive('/about') ? 'font-semibold underline underline-offset-4' : ''}`}
            aria-current={isActive('/about') ? 'page' : undefined}
          >
            About
          </Link>
          <Link
            to="/contact"
            className={`${navLink} ${isActive('/contact') ? 'font-semibold underline underline-offset-4' : ''}`}
            aria-current={isActive('/contact') ? 'page' : undefined}
          >
            Contact Us
          </Link>
          <Link
            to="/contribute"
            className={`${navLink} ${isActive('/contribute') ? 'font-semibold underline underline-offset-4' : ''}`}
            aria-current={isActive('/contribute') ? 'page' : undefined}
          >
            Contribute
          </Link>
        </nav>
      </div>
    </nav>
  );
};

export default Navbar;
