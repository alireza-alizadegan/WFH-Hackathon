import React from 'react'
import logo from "../assets/project.png"

function Header() {
    return (
      <>
        <nav className="navigation">
          <img src={logo} className="user__image" alt="user" />
          <div className="navigation__buttons">
            <button className="navigation__buttons-discover">DISCOVER</button>
            <button className="navigation__buttons-new">NEW PROJECT</button>
          </div>
        </nav>
      </>
    );
}

export default Header
