import React from 'react';
import ReactDOM from 'react-dom/client';

import './style/index.css';

import Views from './components/Views';
import Home from './components/Home';

import SignIn from './components/auth/Signin';
import Otp from './components/auth/Otp';
import SignUp from './components/auth/Signup';

import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Route, Routes } from 'react-router-dom';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Dash />} />
        <Route path="/home" element={<Views />} />

        <Route path='/signup' element={<SignUp />} />
        <Route path='/signin' element={<SignIn />} />
        <Route path='/otp' element={<Otp />} />

        {/* <Route path='/profile' element={<Profile />} />
        <Route path='/social' element={<Social />} />
        <Route path='/culture' element={<Culture />} />
        <Route path='/talents' element={<Talent />} />
        <Route path='/stories' element={<Story />} />
        <Route path='/carries' element={<Carrie />} />
        <Route path='/communities' element={<Community />} />
        <Route path='/news' element={<News />} />
        <Route path='/settings' element={<Settings />} /> */}

      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
