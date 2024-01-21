import { ChatLeftDots, Heart, ReplyAll, Share } from "react-bootstrap-icons";
import '../style/Social.css'


function Social() {

  const username  = "username";

  
  return (
    <div className="Social">

      <div className="post">

        <div className="post-left">

          <div className="post-body">

            <div className="post-header">

              <div className="post-header-left">

                <div className="post-header-img">
                    <img src={username} alt=""  />
                </div>
                
                <div className="post-header-name">{username}</div>

              </div>

              <small className="post-header-time">{username}</small>

            </div>

            <div className="post-content">
                
                <div className="post-content-text">{username}</div>
  
                <div className="post-content-action">
                  <Heart className="post-content-action-like" />
                  <Share className="post-content-action-share" />
                  <ReplyAll className="post-content-action-repost" />
                </div>

            </div>

          </div>

          <div className="post-comment-write">
            <img src={username} alt="" className="post-comment-write-img" />
            <input type="text" className="post-comment-write-input" placeholder="Write a comment..." />
          </div>

        </div>

        <div className="post-right">

          <div className="all-comment">

            <h2>Comments</h2>

            <div className="all-comment-list">

              <div className="comment">

                <div className="comment-header">
                  <img src={username} alt="" className="comment-left-img" />
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
