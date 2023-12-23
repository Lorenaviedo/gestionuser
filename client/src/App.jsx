import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { UsuarioPage } from './pages/UsuarioPage';
import { UsuarioFormPage } from "./pages/UsuarioFormPage";
import { Navbar } from "./components/Navbar";

function App(){
  return(
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Navigate to="/usuario" />} />
        <Route path="/usuario" element={<UsuarioPage />} />
        <Route path="/usuario-crear" element={<UsuarioFormPage />} />
        <Route path="/usuario/:id" element={<UsuarioFormPage />} />
      </Routes>
    </BrowserRouter>
  )
}
export default App;