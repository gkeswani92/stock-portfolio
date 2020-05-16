import React from 'react';
import {
  BrowserRouter as Router,
  Route,
} from 'react-router-dom';
import NavBar from '../NavBar/NavBar';
import Register from '../Register/Register';
import Login from '../Login/Login';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <NavBar />

        <Route path='/login' component={Login} />
        <Route path='/register' component={Register} />
        <Route path='/home' />

      </div>
    </Router>
  );
}

export default App;
