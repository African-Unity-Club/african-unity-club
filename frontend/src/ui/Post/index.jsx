import { Link } from 'react-router-dom';
import { Online } from '../Online';
import { Heart, ReplyAll, Send, Share } from 'react-bootstrap-icons';
import './index.css';


export const Post = ({ post }) => {

    return (
        <div className="post-container">
            <div className="post-header"> 
                <Link to={`/profil/${post.author}`} className='post-header-link'>
                    <Online data={post.data} />
                    <div>{post.author}</div>
                </Link>
                <div className='post-header-date'>{`- ${post.date}`}</div>
            </div>
            <div className="post-content">{post.content}</div>
            <div className="post-action">
                <div className='post-action-click'>
                    <span className='post-action-icon'>
                        <Heart size={20} />
                        <span className='post-action-number'>{post.action.likes}</span>
                    </span>
                    <span className='post-action-icon'>
                        <ReplyAll size={20} />
                        <span className='post-action-number'>{post.action.reply}</span>
                    </span>
                    <span className='post-action-icon'>
                        <Share size={20} />
                        <span className='post-action-number'>{post.action.share}</span>
                    </span>
                </div>
                <div className='post-action-comments'>
                    <Link to={`/post/${post.id}`} className='post-action-comments-link'>
                        <span className='post-action-comments-number'>{post.action.comment}</span>
                        <span className='post-action-comments-text'>Comments</span>
                    </Link>
                </div>
            </div>
            <div className="post-users-react">
                {
                    post.react.map((user) => {
                        return (
                            <Link key={user.key} to={`/profil/${user.author}`}>
                                <Online data={user.data} />
                            </Link>
                        )
                    })
                }
            </div>
            <div className="post-comment-writer">
                <Online data={post.current.data} />
                <textarea className='post-comment-input' placeholder='write your comment'></textarea>
                <Send className='post-comment-send' onClick={``} />
            </div>
        </div>
    )
}
