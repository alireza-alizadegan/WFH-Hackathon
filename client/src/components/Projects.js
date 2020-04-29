import React from 'react'

function Projects() {
    return (
      <>
        <div className="project">
          <h2 className="project__title">Your Projects</h2>
          <div className="project__container">
            <div className="project__card">
              <h5 className="project__card-name">First Project</h5>
              <p className="project__card-time">Time Remaining: </p>
              <p className="project__card-participants">Participants:</p>
            </div>

            <div className="project__card">
              <h5 className="project__card-name">Second Project</h5>
              <p className="project__card-time">Time Remaining: </p>
              <p className="project__card-participants">Participants:</p>
            </div>

            <div className="project__card">
              <h5 className="project__card-name">Third Project</h5>
              <p className="project__card-time">Time Remaining: </p>
              <p className="project__card-participants">Participants:</p>
            </div>

            <div className="project__card">
              <h5 className="project__card-name">Fourth Project</h5>
              <p className="project__card-time">Time Remaining: </p>
              <p className="project__card-participants">Participants:</p>
            </div>

            <div className="project__card">
              <h5 className="project__card-name">Fifth Project</h5>
              <p className="project__card-time">Time Remaining: </p>
              <p className="project__card-participants">Participants:</p>
            </div>
          </div>
        </div>
      </>
    );
}

export default Projects
