import { ChatLeftDots, Heart, ReplyAll, Share } from "react-bootstrap-icons";
import '../../style/Social.css'
import { Link } from 'react-router-dom'
import Anonymous from '../../assets/nouser.png'


function Social() {

  const username  = "username";

  
  return (
    <div className="Social">

      <div className="post-list">
        
        <div className="post">

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
            {`
                Ajoutez des annexes pour inclure des informations supplémentaires, telles que des CV d'équipe, des études de marché détaillées, etc.
                En suivant ces étapes, vous pouvez créer un business plan complet et convaincant. N'oubliez pas de le mettre à jour régulièrement pour refléter les changements dans votre entreprise et dans l'environnement commercial.
            `}
          </div>
          <div className="action">
            <div className="post-action-left">
              <Heart className="post-action-like" size={20} />
              <Share className="post-action-share" size={20} />
              <ReplyAll className="post-action-repost" size={20} />
            </div>
            <div className="post-action-rigth">
              <Link to={``} className="post-comment-link">comments</Link>
              <span className="post-count-repost">
                <span className="post-count">567</span>
                repost
              </span>
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

      </div>
      
    </div>
  );
}

export default Social;
