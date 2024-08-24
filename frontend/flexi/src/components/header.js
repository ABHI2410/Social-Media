import React, { useState } from "react";
import Navigation from "../components/navigation";
import catlogo from "../catlogo.svg";

const Header = () => {
  const [isNavOpen, setIsNavOpen] = useState(true);

  const toggleNav = () => {
    setIsNavOpen(!isNavOpen);
  };

  return (
    <header className="fixed top-0 left-0 right-0 border-b-2 bg-white z-50">
      <nav
        className="mr-auto flex max-w-7xl items-center lg:px-8"
        aria-label="Global"
      >
        <div className="flex items-left lg:hidden">
          <button
            type="button"
            className="text-gray-800 p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-inset focus:ring-gray-600"
            onClick={toggleNav}
          >
            <svg
              className="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M4 6h16M4 12h16m-7 6h7"
              ></path>
            </svg>
            <span className="sr-only">Open Navigation</span>
          </button>
        </div>

        <div className="flex flex-row lg:flex-1">
          <a href="/" className="-m-1.5 p-1.5 flex items-center">
            <img className="h-16 w-auto" src={catlogo} alt="Felix Logo" />
            <span className="ml-2 font-bold text-4xl tracking-wide">Felix</span>
          </a>
        </div>

        <div className="flex flex-1 justify-end mr-2">
          <div>
            <button
              type="button"
              className="flex text-sm bg-gray-800 rounded-full focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600"
            >
              <span className="sr-only">Open user menu</span>
              <img
                className="w-8 h-8 rounded-full"
                src="https://flowbite.com/docs/images/people/profile-picture-5.jpg"
                alt="user profile"
              />
            </button>
          </div>
        </div>
      </nav>

      {isNavOpen ? <Navigation toggleNav={toggleNav} /> : null}
    </header>
  );
};

export default Header;
