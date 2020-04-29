import React from 'react'
import Profile from './Profile'
import Interests from './Interests'
import Projects from "./Projects";

function Home() {
    return (
      <div className="main">
        <Profile />
        <Interests />
        <Projects />
      </div>
    );
}

export default Home
