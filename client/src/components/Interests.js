import React, { Component } from 'react'

export default class Interests extends Component {
    constructor(props) {
        super(props)

    }
    render() {
        return (
          <div className="middle">
            <div className="interests">
              <h2 className="interests__title">Interests</h2>
              <div className="interest">
                <div className="interest__subject">
                  <h4 className="interest__subject-title">Subject</h4>
                  <ul className="interest__subject-name">
                    <li className="interest__subject-name--one">Technology</li>
                    <li className="interest__subject-name--two">Sports</li>
                    <li className="interest__subject-name--three">Arts</li>
                  </ul>
                </div>
                {/* end of subject card  */}

                <div className="interest__rate">
                  <h4 className="interest__rate-title">Rate</h4>
                  <ul className="interest__rate-name">
                    <li className="interest__rate-name--one">5</li>
                    <li className="interest__rate-name--two">3</li>
                    <li className="interest__rate-name--three">1</li>
                  </ul>
                </div>
                {/* end of rate card */}

                <div className="interest__exp">
                  <h4 className="interest__exp-title">Experience</h4>
                  <ul className="interest__exp-name">
                    <li className="interest__exp-name--one">5</li>
                    <li className="interest__exp-name--two">3</li>
                    <li className="interest__exp-name--three">1</li>
                  </ul>
                </div>
                {/* end of experience card */}
              </div>
            </div>

            <div className="profile__projects">
              <h2 className="profile__completed-projects">Complete Projects</h2>
              <div className="profile__completed-projects--number">
                0 Completed Projects
              </div>
            </div>
          </div>
        );
    }
}
