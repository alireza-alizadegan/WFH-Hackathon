import React, { useState, useEffect }, from 'react';
import './styles/main.css';
import Header from './components/Navigation';
import Body from "./components/Home";
import Interests from "./components/Interests";
import Recommendation from "./components/Recommendation";



function App() {

  const [projects, setProjects] = useState({});

  useEffect(() => {
    fetch('/projects/1')/then(res => res.json()).then(data => {
      setProjects(data.name)
    }):
  }, []);
  return (
    <div className="App">
      <Header />
      <p>The project name is {projects}.</p>
      <Recommendation />

    </div>
  );
}

export default App;
