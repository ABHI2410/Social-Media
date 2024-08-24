import React from "react";

const Navigation = () => {
  return (
    <>
      <div
        id="drawer-navigation"
        className="fixed left-0 top-[70px] z-40 w-full md:w-56 h-[calc(100vh-80px)] p-4 overflow-y-auto transition-transform bg-white border-r-2"
        aria-labelledby="drawer-navigation-label"
      >
        {/* Navigation Items */}
        <div className="pt-6 overflow-y-auto">
          <ul className="space-y-2 p-t-2 font-medium">
            <li>
              <a
                href="/"
                className="flex items-center p-2 text-gray-900 rounded-lg bg-gray-100 hover:bg-gray-700 group"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  height="24px"
                  viewBox="0 -960 960 960"
                  width="24px"
                  fill="#9ca3af"
                >
                  <path d="M240-200h120v-240h240v240h120v-360L480-740 240-560v360Zm-80 80v-480l320-240 320 240v480H520v-240h-80v240H160Zm320-350Z" />
                </svg>
                <span className="ms-3">Home</span>
              </a>
            </li>
            <li>
              <a
                href="/"
                className="flex items-center p-2 text-gray-900 rounded-lg hover:bg-gray-700 group"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  height="24px"
                  viewBox="0 -960 960 960"
                  width="24px"
                  fill="#9ca3af"
                >
                  <path d="m136-240-56-56 296-298 160 160 208-206H640v-80h240v240h-80v-104L536-320 376-480 136-240Z" />
                </svg>
                <span className="flex-1 ms-3 whitespace-nowrap">
                  Flexi Space
                </span>
              </a>
            </li>
          </ul>
          {/* Subscribed Flexi Space */}
          <ul className="pt-4 mt-4 h-96 space-y-2 font-medium border-t border-gray-200 dark:border-gray-700">
            <span className="flex-1 text-xs whitespace-nowrap">Subscribed</span>
            <li>
              <a
                href="/"
                className="flex items-center p-2 text-gray-900 rounded-lg hover:bg-gray-700 group"
              >
                <span className="flex-1 ms-3 whitespace-nowrap">
                  Flexi Space
                </span>
                <span className="inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-white bg-blue-100 rounded-full dark:bg-blue-600 dark:text-white">
                  3
                </span>
              </a>
            </li>
            <span className="flex justify-end text-xs whitespace-nowrap">
              ...More
            </span>
          </ul>
          {/* Sign In / Sign Up */}
          <ul className="bottom-0 pt-4 mt-4 space-y-2 font-medium border-t border-gray-200 dark:border-gray-700">
            <li>
              <a
                href="/"
                className="flex items-center p-2 text-gray-900 rounded-lg hover:bg-gray-700 group"
              >
                <svg
                  className="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 18 16"
                >
                  <path
                    stroke="currentColor"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3"
                  />
                </svg>
                <span className="flex-1 ms-3 whitespace-nowrap">Sign In</span>
              </a>
            </li>
            <li>
              <a
                href="/"
                className="flex items-center p-2 text-gray-900 rounded-lg hover:bg-gray-700 group"
              >
                <svg
                  className="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path d="M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z" />
                  <path d="M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 2 2h11v-1.933a4.852 4.852 0 0 1-1.289-.336l-6.107-6.107a2.963 2.963 0 0 1-.867-.563Z" />
                  <path d="M19.248 12.305a3.004 3.004 0 0 0-4.24 0L8.585 18.73a1 1 0 0 0-.272.455l-1 3a1 1 0 0 0 1.232 1.232l3-1a1 1 0 0 0 .455-.272l6.423-6.423a3.004 3.004 0 0 0 0-4.24Z" />
                </svg>
                <span className="flex-1 ms-3 whitespace-nowrap">Sign Up</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </>
  );
};

export default Navigation;
