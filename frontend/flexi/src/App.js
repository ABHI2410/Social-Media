// import logo from './logo.svg';
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Flexi from "./pages/index";

function App() {
  return (
    <div style={{ height: "100%" }}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Flexi />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
