import React from 'react';
import {
  BrowserRouter as Router,
  Route,
} from 'react-router-dom';
import NavBar from '../NavBar/NavBar';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <NavBar />

        <Route path='/login' />
        <Route path='/register' />
        <Route path='/home' />

      </div>
    </Router>
  );
}

export default App;
