import { ArrowLeftCircle, BlockquoteLeft, Briefcase, GraphDownArrow, Newspaper, People, PersonGear, Quote, Sliders, Stars, YinYang } from 'react-bootstrap-icons';
import { Link } from 'react-router-dom';


const SideNav = ({ props }) => {

    const logo = '../../assets/noprofile.jpeg'
    return (
        <div className="sidenav">
            <div className="sidenav-header">
                <div className="userlogo">
                    <img src={logo} alt='' />
                    <span className="online"></span>
                </div>
                <span className="username">{props.username}</span>
            </div>
            <nav className="sidenav-body">
                <Link to={`/dashboard/${props.username}`} className="sidenav-link">
                    <GraphDownArrow size={20} />
                    Dashboard
                </Link>
                <Link to={`/profile/${props.username}`} className="sidenav-link">
                    <PersonGear size={20}/>
                    Profile</Link>
                <Link to="/social" className="sidenav-link">
                    <Quote size={20}/>
                    Social</Link>
                <Link to="/cultures" className="sidenav-link">
                    <YinYang size={20}/>
                    Cultures</Link>
                <Link to="/talents" className="sidenav-link">
                    <Stars size={20}/>
                    Talents</Link>
                <Link to="/stories" className="sidenav-link">
                    <BlockquoteLeft size={20}/>
                    Stories</Link>
                <Link to="/careers" className="sidenav-link">
                    <Briefcase size={20}/>
                    Careers</Link>
                <Link to="/communities" className="sidenav-link">
                    <People size={20}/>
                    Communities</Link>
                <Link to="/news" className="sidenav-link">
                    <Newspaper size={20}/>
                    News</Link>
                <Link to={`/settings/${props.username}`} className="sidenav-link">
                    <Sliders size={20}/>
                    Settings</Link>
            </nav>
            <div className="sidenav-footer">
                <Link to="/logout" className="sidenav-link">
                    <ArrowLeftCircle size={20} />
                    Logout
                </Link>
            </div>
        </div>
    )
}

export default SideNav
