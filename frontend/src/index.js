import React from 'react';
import ReactDOM from 'react-dom/client';

import './style/index.css';

import Views from './components/Views';

import SignIn from './components/auth/Signin';
import VerifyOtp from './components/auth/Otp';
import SignUp from './components/auth/Signup';
import Forgot from './components/auth/Forgot';
import ResetPassword from './components/auth/Reset';

import Social from './components/Home/Social';
import Index from './components/Index';

import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Route, Routes } from 'react-router-dom';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/home" element={<Views />} />

        <Route path='/signup' element={<SignUp />} />
        <Route path='/signin' element={<SignIn />} />
        <Route path='/otp' element={<VerifyOtp />} />
        <Route path='/forgot' element={<Forgot />} />
        <Route path='/reset' element={<ResetPassword />} />
        
        <Route path='/' element={<Index />} >
          <Route path='' element={<Social />} />
        </Route>
        

        

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
