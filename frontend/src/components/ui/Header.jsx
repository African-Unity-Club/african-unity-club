import { Link } from 'react-router-dom';
import '../../style/All.css';


const Header = ({ props }) => {

    return (
        
        <header className="header">
            <div className="header-body">
                <Link to="/" className="header-link">
                    <span className='logo'></span>
                    Dream Africa
                </Link>
                <div className="header-search">
                    <select className="header-search-select">
                        <option value="all">
                            <i className="fas fa-globe-africa"></i>
                            <span className="area-item-name">All</span>
                        </option>
                        {
                            props.seo.map((search, index) => (
                                <option value={search.name} key={index}>
                                    <i className={search.icon}></i>
                                    <span className="area-item-name">{search.name}</span>
                                </option>
                            ))
                        }
                    </select>
                    <input type="text" className="header-search-input" placeholder="Search Dream Africa" />
                    <button className="header-search-button">Search</button>
                </div>
            </div>
            <div className="header-footer">
                <h1 className="header-title">{`Dashboard`}</h1>
                <nav className="header-nav">
                    <Link to={`/calendar/${props.username}`} className="header-link">
                        <i className="far fa-calendar-alt"></i>
                    </Link>
                    <Link to={`/notification/${props.username}`} className="header-link">
                        <i className="far fa-envelope"></i>
                        <span className='total'>104</span>
                    </Link>
                    <Link to={`/message/${props.username}`} className="header-link">
                        <i className="far fa-user"></i>
                        <span className='total'>104</span>
                    </Link>
                    <Link to={`/friendish/${props.username}`} className="header-link">
                        <i className="far fa-user"></i>
                        <span className='total'>104</span>
                    </Link>
                </nav>
            </div>
        </header>
    )
}

export default Header;
