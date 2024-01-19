import { Link } from 'react-router-dom';
import '../../style/All.css';
import { Search, Bell, ChatLeft, PersonCircle, Calendar2Date } from 'react-bootstrap-icons'


const Header = ({ props }) => {

    return (
        
        <header className="header">
            <div className="header-body">
                <Link to="/" className="header-link">
                    <span className='logo'></span>
                    Dream Africa
                </Link>
                <div className="header-search">
                    <input type="text" className="header-search-input" placeholder="Search Dream Africa" />
                    <button className="header-search-button">
                        <Search size={24} color='aliceblue'/>
                    </button>
                </div>
            </div>
            <div className="header-footer">
                <h1 className="header-title">{`Dashboard`}</h1>
                <nav className="header-nav">
                    <Link to={`/calendar/${props.username}`} className="header-link">
                        <Calendar2Date size={20} />
                    </Link>
                    <Link to={`/notification/${props.username}`} className="header-link">
                        <Bell size={20} />
                        <span className='total'>104</span>
                    </Link>
                    <Link to={`/message/${props.username}`} className="header-link">
                        <ChatLeft size={20} />
                        <span className='total'>104</span>
                    </Link>
                    <Link to={`/friendish/${props.username}`} className="header-link">
                        <PersonCircle size={20} />
                        <span className='total'>104</span>
                    </Link>
                </nav>
            </div>
        </header>
    )
}

export default Header;
