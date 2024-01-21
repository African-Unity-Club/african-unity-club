import { ChatLeftDots, Heart, ReplyAll, Share } from "react-bootstrap-icons";
import '../style/Social.css'
import { Link } from 'react-router-dom'
import Anonymous from '../assets/nouser.png'


function Social() {

  const username  = "username";

  
  return (
    <div className="Social">

      <div className="post">

        <div className="post-left">

          <div className="post-body">

            <div className="post-header">

              <Link to="ddddd" className="post-header-left">

              <div className="userlogo soc-icon">
                <img src={Anonymous} alt="" className="userlogo-img" />
                <span className="online">
                  <span className="online-dot"></span>
                </span>
              </div>

                <div className="post-header-name">{username}</div>

              </Link>

              <small className="post-header-time">{username}</small>

            </div>

            <div className="post-content">
                
                <div className="post-content-text">
                  {`
                    Ajoutez des annexes pour inclure des informations supplémentaires, telles que des CV d'équipe, des études de marché détaillées, etc.
                    En suivant ces étapes, vous pouvez créer un business plan complet et convaincant. N'oubliez pas de le mettre à jour régulièrement pour refléter les changements dans votre entreprise et dans l'environnement commercial.
                  `}
                </div>
  
                <div className="post-content-action">
                  <Heart className="post-content-action-like" size={20} />
                  <Share className="post-content-action-share" size={20} />
                  <ReplyAll className="post-content-action-repost" size={20} />
                </div>

            </div>

          </div>

          <div className="post-comment-write">
            <div className="userlogo soc-icon">
              <img src={Anonymous} alt="" className="userlogo-img" />
              <span className="online">
                <span className="online-dot"></span>
              </span>
            </div>
            <textarea name="" id="" cols="30" rows="10" className="post-comment-write-input"></textarea>
          </div>

        </div>

        <div className="post-right">

          <div className="all-comment">

            <h2>Comments</h2>

            <div className="all-comment-list">

              <div className="comment">

                <div className="comment-header">
                  <div className="userlogo soc-icon">
                    <img src={Anonymous} alt="" className="userlogo-img" />
                    <span className="online">
                      <span className="online-dot"></span>
                    </span>
                  </div>
                  <span className="comment-left-name">{username}</span>
                </div>

                <div className="comment-body">

                  <div className="comment-content">
                    {`
                      Ajoutez des annexes pour inclure des informations supplémentaires, telles que des CV d'équipe, des études de marché détaillées, etc. En suivant ces étapes, vous pouvez créer un business plan complet et convaincant. N'oubliez pas de le mettre à jour régulièrement pour refléter les changements dans votre entreprise et dans l'environnement commercial.
                    `}
                  </div>
                  <div className="comment-action">
                    <span>
                      <span>1002</span>
                      <span>Like</span>
                    </span>
                    <span>
                      <span>1002</span>
                      <span>reply</span>
                    </span>
                  </div>

                </div>

              </div>

              <div className="comment-reply">
                <div className="comment-previous">
                  <div className="userlogo soc-icon">
                    <img src={Anonymous} alt="" className="userlogo-img" />
                    <span className="online">
                      <span className="online-dot"></span>
                    </span>
                  </div>
                  <div className="reply-content">
                    kjdididzijfdozfdjzlskdmkpskdp...
                  </div>
                </div>
                <div className="comment">

                  <div className="comment-header">
                    <div className="userlogo soc-icon">
                      <img src={Anonymous} alt="" className="userlogo-img" />
                      <span className="online">
                        <span className="online-dot"></span>
                      </span>
                    </div>
                    <span className="comment-left-name">{username}</span>
                  </div>

                  <div className="comment-body">

                  <div className="comment-content">
                    {`
                      Ajoutez des annexes pour inclure des informations supplémentaires, telles que des CV d'équipe, des études de marché détaillées, etc. En suivant ces étapes, vous pouvez créer un business plan complet et convaincant. N'oubliez pas de le mettre à jour régulièrement pour refléter les changements dans votre entreprise et dans l'environnement commercial.
                    `}
                  </div>
                  <div className="comment-action">
                    <span>
                      <span>1002</span>
                      <span>Like</span>
                    </span>
                  </div>

                  </div>

                </div>
              </div>
            </div>

          </div>

          <div className="new-post">
            <input type="text" className="new-post-input" placeholder="Write a comment..." />
            <a href="sjnsdl" className="new-post-button">+</a>
          </div>

        </div>

      </div>

    </div>
  );
}

export default Social;
