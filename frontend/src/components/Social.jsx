import { ChatLeftDots, Heart, ReplyAll, Share } from "react-bootstrap-icons";
import '../style/Social.css'
import { Link } from 'react-router-dom'


function Social() {

  const username  = "username";

  
  return (
    <div className="Social">

      <div className="post">

        <div className="post-left">

          <div className="post-body">

            <div className="post-header">

              <Link to="ddddd" className="post-header-left">

                <div className="post-header-img">
                    <img src={username} alt=""  />
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
            <span className="post-comment-write-img">
              <img src={username} alt="" />
            </span>
            <textarea name="" id="" cols="30" rows="10" className="post-comment-write-input"></textarea>
          </div>

        </div>

        <div className="post-right">

          <div className="all-comment">

            <h2>Comments</h2>

            <div className="all-comment-list">

              <div className="comment">

                <div className="comment-header">
                  <img src={username} alt="" />
                  <span className="comment-left-name">{username}</span>
                </div>

                <div className="comment-body">

                  <div className="comment-content">{username}</div>
                  <div className="comment-action">
                    <Heart className="comment-action-like" />
                    <ChatLeftDots className="comment-action-response" />
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
