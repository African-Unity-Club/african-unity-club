import { ChatLeftDots, Heart, ReplyAll, Send, Share } from "react-bootstrap-icons";
import './Social.css'
import { Link } from 'react-router-dom'
import { Online } from "../../ui/Online";

function Social() {

  const username  = "username";

  
  return (
    <div className="Social">

      <div className="social-left">

        <div className="social-post-writer">
          <Online data={{ dim: 'mini', status: true }} />
          <Link to='/' className="writer">write your post</Link>
        </div>

        <div className="social-post-list">

          <div className="social-post">

            <div className="social-post-header">

              <Link to={``} className="social-post-header-left">
                <Online data={{ dim: 'mini', status: true }} />
                <div className="post-header-name">{username}</div>
              </Link>
              <div className="social-post-header-right">
                -- yesterday
              </div>

            </div>

            <div className="social-post-content">
              {`
                Ajoutez des annexes pour inclure des informations supplémentaires, telles que des CV d'équipe, des études de marché détaillées, etc.
                En suivant ces étapes, vous pouvez créer un business plan complet et convaincant. N'oubliez pas de le mettre à jour régulièrement pour refléter les changements dans votre entreprise et dans l'environnement commercial.
              `}
            </div>

            <div className="social-post-action">

              <div className="social-post-action-left">

                <span className="social-post-action-body">
                  <Heart className="social-post-action-like" size={20} />
                  <span className="social-post-elt-count">4.8k</span>
                </span>

                <span className="social-post-action-body">
                  <Share className="social-post-action-share" size={20} />
                  <span className="social-post-elt-count">4.8k</span>
                </span>

                <span className="social-post-action-body">
                  <ReplyAll className="social-post-action-repost" size={24} />
                  <span className="social-post-elt-count">4.8k</span>
                </span>

              </div>

              <div className="social-post-action-rigth">
                <Link to={``} className="social-post-comment-link">comments</Link>
              </div>

            </div>

            <div className="social-user-reaction">
              <Link to={``}>
                <Online data={{ dim: 'x-mini', status: true}} />
              </Link>
              <Link to={``}>
                <Online data={{ dim: 'x-mini', status: true}} />
              </Link>
              <Link to={``}>
                <Online data={{ dim: 'x-mini', status: true}} />
              </Link>
              <Link to={``}>
                <span className="userlogo-img">...</span>
              </Link>
            </div>

            <div className="social-post-comment">
              <div >
                <Online data={{ dim: 'mini', status: true}} />
              </div>
              <textarea className="social-post-comment-input" placeholder="write your comment"></textarea>
              <Send className="social-post-comment-send" onClick={``} />
            </div>

          </div>

          <div className="social-post">

            <div className="social-post-header">

              <Link to={``} className="social-post-header-left">
                <Online data={{ dim: 'mini', status: true }} />
                <div className="post-header-name">{username}</div>
              </Link>
              <div className="social-post-header-right">
                -- yesterday
              </div>

            </div>

            <div className="social-post-content">
              {`
                Ajoutez des annexes pour inclure des informations supplémentaires, telles que des CV d'équipe, des études de marché détaillées, etc.
                En suivant ces étapes, vous pouvez créer un business plan complet et convaincant. N'oubliez pas de le mettre à jour régulièrement pour refléter les changements dans votre entreprise et dans l'environnement commercial.
              `}
            </div>

            <div className="social-post-action">

              <div className="social-post-action-left">

                <span className="social-post-action-body">
                  <Heart className="social-post-action-like" size={20} />
                  <span className="social-post-elt-count">4.8k</span>
                </span>

                <span className="social-post-action-body">
                  <Share className="social-post-action-share" size={20} />
                  <span className="social-post-elt-count">4.8k</span>
                </span>

                <span className="social-post-action-body">
                  <ReplyAll className="social-post-action-repost" size={24} />
                  <span className="social-post-elt-count">4.8k</span>
                </span>

              </div>

              <div className="social-post-action-rigth">
                <Link to={``} className="social-post-comment-link">comments</Link>
              </div>

            </div>

            <div className="social-user-reaction">

              <Link to={``}>
                <Online data={{ dim: 'x-mini', status: true}} />
              </Link>
              <Link to={``}>
                <Online data={{ dim: 'x-mini', status: true}} />
              </Link>
              <Link to={``}>
                <Online data={{ dim: 'x-mini', status: true}} />
              </Link>
              <Link to={``}>
                <span className="userlogo-img">...</span>
              </Link>
            </div>

            <div className="social-post-comment">
              <div>
                <Online data={{ dim: 'mini', status: true}} />
              </div>
              <textarea className="social-post-comment-input" placeholder="write your comment"></textarea>
              <Send className="social-post-comment-send" onClick={``} />
            </div>

          </div>

          <div className="social-post">

            <div className="social-post-header">

              <Link to={``} className="social-post-header-left">
                <Online data={{ dim: 'mini', status: true }} />
                <div className="post-header-name">{username}</div>
              </Link>
              <div className="social-post-header-right">
                -- yesterday
              </div>

            </div>

            <div className="social-post-content">
              {`
                Ajoutez des annexes pour inclure des informations supplémentaires, telles que des CV d'équipe, des études de marché détaillées, etc.
                En suivant ces étapes, vous pouvez créer un business plan complet et convaincant. N'oubliez pas de le mettre à jour régulièrement pour refléter les changements dans votre entreprise et dans l'environnement commercial.
              `}
            </div>

            <div className="social-post-action">

              <div className="social-post-action-left">

                <span className="social-post-action-body">
                  <Heart className="social-post-action-like" size={20} />
                  <span className="social-post-elt-count">4.8k</span>
                </span>

                <span className="social-post-action-body">
                  <Share className="social-post-action-share" size={20} />
                  <span className="social-post-elt-count">4.8k</span>
                </span>

                <span className="social-post-action-body">
                  <ReplyAll className="social-post-action-repost" size={24} />
                  <span className="social-post-elt-count">4.8k</span>
                </span>

              </div>

              <div className="social-post-action-rigth">
                <Link to={``} className="social-post-comment-link">comments</Link>
              </div>

            </div>

            <div className="social-user-reaction">

              <Link to={``}>
                <Online data={{ dim: 'x-mini', status: true}} />
              </Link>
              <Link to={``}>
                <Online data={{ dim: 'x-mini', status: true}} />
              </Link>
              <Link to={``}>
                <Online data={{ dim: 'x-mini', status: true}} />
              </Link>
              <Link to={``}>
                <span className="userlogo-img">...</span>
              </Link>
            </div>

            <div className="social-post-comment">
              <div>
                <Online data={{ dim: 'mini', status: true}} />
              </div>
              <textarea className="social-post-comment-input" placeholder="write your comment"></textarea>
              <Send className="social-post-comment-send" onClick={``} />
            </div>

          </div>

          <div className="social-post">

            <div className="social-post-header">

              <Link to={``} className="social-post-header-left">
                <Online data={{ dim: 'mini', status: true }} />
                <div className="post-header-name">{username}</div>
              </Link>
              <div className="social-post-header-right">
                -- yesterday
              </div>

            </div>

            <div className="social-post-content">
              {`
                Ajoutez des annexes pour inclure des informations supplémentaires, telles que des CV d'équipe, des études de marché détaillées, etc.
                En suivant ces étapes, vous pouvez créer un business plan complet et convaincant. N'oubliez pas de le mettre à jour régulièrement pour refléter les changements dans votre entreprise et dans l'environnement commercial.
              `}
            </div>

            <div className="social-post-action">

              <div className="social-post-action-left">

                <span className="social-post-action-body">
                  <Heart className="social-post-action-like" size={20} />
                  <span className="social-post-elt-count">4.8k</span>
                </span>

                <span className="social-post-action-body">
                  <Share className="social-post-action-share" size={20} />
                  <span className="social-post-elt-count">4.8k</span>
                </span>

                <span className="social-post-action-body">
                  <ReplyAll className="social-post-action-repost" size={24} />
                  <span className="social-post-elt-count">4.8k</span>
                </span>

              </div>

              <div className="social-post-action-rigth">
                <Link to={``} className="social-post-comment-link">comments</Link>
              </div>

            </div>

            <div className="social-user-reaction">

              <Link to={``}>
                <Online data={{ dim: 'x-mini', status: true}} />
              </Link>
              <Link to={``}>
                <Online data={{ dim: 'x-mini', status: true}} />
              </Link>
              <Link to={``}>
                <Online data={{ dim: 'x-mini', status: true}} />
              </Link>
              <Link to={``}>
                <span className="userlogo-img">...</span>
              </Link>
            </div>

            <div className="social-post-comment">
              <div>
                <Online data={{ dim: 'mini', status: true}} />
              </div>
              <textarea className="social-post-comment-input" placeholder="write your comment"></textarea>
              <Send className="social-post-comment-send" onClick={``} />
            </div>

          </div>

        </div>
      </div>

      <div className="social-right">

      </div>
      

    </div>
  );
}

export default Social;
