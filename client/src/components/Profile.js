import React from 'react'
import user from "../assets/blank-user.png"

function Profile() {
    return (
      <>
        <div className="profile">
          <h2 className="profile__title">Profile</h2>
          <div className="profile__info">
            <div className="profile__user">
              <img className="profile__user-image" src={user} alt="user" />
              <h4 className="profile__user-name">John Doe</h4>
              <p className="profile__user-description">Biography</p>
            </div>
            <input className="profile__info-location" placeholder="Location" />
            <input className="profile__info-age" placeholder="Age" />
            <input className="profile__info-position" placeholder="Position" />
            <input className="profile__info-time" placeholder="Time" />
          </div>
          {/* <div className="profile__projects">
            <h3 className="profile__completed-projects">Complete Projects</h3>
            <div className="profile__completed-projects--number">0 Completed Projects</div>
        </div> */}
        </div>
      </>
    );
}

export default Profile
