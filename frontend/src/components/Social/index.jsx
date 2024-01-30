import { Heart, ReplyAll, Send, Share } from "react-bootstrap-icons";
import './index.css';
import { Link } from 'react-router-dom';
import { Online } from "../../ui/Online";
import { Post } from "../../ui/Post";


function Social() {

  const username  = "username";

  const post = {
    author: 'jean',
    id: 'sfljflefjodvf',
    data: {
      dim: 'mini',
      status: true
    },
    date: 'yesterday',
    content: "Ajoutez des annexes pour inclure des informations supplémentaires," +
      "telles que des CV d'équipe, des études de marché détaillées, etc." +
      "En suivant ces étapes, vous pouvez créer un business plan complet et convaincant." +
      "N'oubliez pas de le mettre à jour régulièrement pour refléter les changements dans votre" +
      "entreprise et dans l'environnement commercial.",
    action: {
      likes: 243,
      reply: 987,
      share: 2,
      comment: 897
    },
    react: [
      {
        key: 'henry-14',
        author: 'henry',
        data: {
          dim: 'x-mini',
          status: true
        }
      },
      {
        key: 'joseph-17',
        author: 'joseph',
        data: {
          dim: 'x-mini',
          status: true
        }
      },
      {
        key: 'kratos-20',
        author: 'kratos',
        data: {
          dim: 'x-mini',
          status: true
        }
      }
    ],
    current: {
      data: {
        dim: 'mini',
        status: true
      }
    }
  }

  
  return (
    <div className="Social">

      <div className="social-left">
        <div className="social-post-list">

          <Post post={post} />
          <Post post={post} />
          <Post post={post} />

        </div>
      </div>
    </div>
  );
}

export default Social;
