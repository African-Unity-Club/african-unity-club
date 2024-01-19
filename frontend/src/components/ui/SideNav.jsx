import { Link } from 'react-router-dom';


const SideNav = ({ props }) => {


    return (
        <div className="sidenav">
            <div className="sidenav-header">
                <div className="userlogo">
                    <span className="online"></span>
                </div>
                <span className="username">{props.username}</span>
            </div>
            <nav className="sidenav-body">
                <Link to={`/dashboard/${props.username}`} className="sidenav-link">Dashboard</Link>
                <Link to={`/profile/${props.username}`} className="sidenav-link">Profile</Link>
                <Link to="/social" className="sidenav-link">Social</Link>
                <Link to="/cultures" className="sidenav-link">Cultures</Link>
                <Link to="/talents" className="sidenav-link">Talents</Link>
                <Link to="/stories" className="sidenav-link">Stories</Link>
                <Link to="/careers" className="sidenav-link">Careers</Link>
                <Link to="/communities" className="sidenav-link">Communities</Link>
                <Link to="/news" className="sidenav-link">News</Link>
                <Link to={`/settings/${props.username}`} className="sidenav-link">Settings</Link>
            </nav>
            <div className="sidenav-footer">
                <Link to="/logout" className="sidenav-link">Logout</Link>
            </div>
        </div>
    )
}

export default SideNav
