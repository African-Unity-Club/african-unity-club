import { 
    ArrowLeftCircle,
    BlockquoteLeft,
    Briefcase,
    GraphDownArrow,
    Newspaper,
    People,
    PersonGear,
    Quote,
    Sliders,
    Stars,
    YinYang,
    Search,
    Bell,
    ChatLeft,
    PersonCircle,
    Calendar2Date 
} from 'react-bootstrap-icons';

import { Link, Outlet } from 'react-router-dom';
import '../style/All.css'
import Anonymous from '../assets/nouser.png'
import { Online } from '../ui/Online'


function Index() {

    const username = 'unknown'
    let online = true

    return (
        <main className="index-main">

            <aside className="left-side-nav-bar">
                
                <div className="side-nav-bar-header">

                    <Online data={{ status: online }}/>

                    <span className="username">
                        {username}
                        <small>{online ? 'online' : '2 min'}</small>
                    </span>

                </div>

                <nav className="side-body">
                    <Link to={`/dashboard/${username}`} className="body-side-nav-link dashboard">
                        <GraphDownArrow size={20} />
                        Dashboard
                    </Link>
                    <Link to={`/profile/${username}`} className="body-side-nav-link profile">
                        <PersonGear size={20}/>
                        Profile</Link>
                    <Link to="/" className="body-side-nav-link social">
                        <Quote size={20}/>
                        Social</Link>
                    <Link to="/cultures" className="body-side-nav-link culture">
                        <YinYang size={20}/>
                        Cultures</Link>
                    <Link to="/talents" className="body-side-nav-link talent">
                        <Stars size={20}/>
                        Talents</Link>
                    <Link to="/stories" className="body-side-nav-link storie">
                        <BlockquoteLeft size={20}/>
                        Stories</Link>
                    <Link to="/careers" className="body-side-nav-link careers">
                        <Briefcase size={20}/>
                        Careers</Link>
                    <Link to="/communities" className="body-side-nav-link communities">
                        <People size={20}/>
                        Communities</Link>
                    <Link to="/news" className="body-side-nav-link news">
                        <Newspaper size={20}/>
                        News</Link>
                    <Link to={`/settings/${username}`} className="body-side-nav-link settings">
                        <Sliders size={20}/>
                        Settings</Link>
                </nav>

                <div className="side-footer">
                    <Link to="/logout" className="footer-side-link">
                        <ArrowLeftCircle size={20} />
                        Logout
                    </Link>
                </div>

            </aside>

            <section className='body-container'>

                <header className='header-content-nav-bar'>

                    <Link to="/" className="header-link">
                        <span className='logo'></span>
                        Land Of Peace
                    </Link>

                    <div className="header-search">
                        <input type="text" className="header-search-input" placeholder="Search Land Of Peace" />
                        <button className="header-search-button">
                            <Search size={20} color='aliceblue'/>
                        </button>
                    </div>

                </header>

                <div className='container'>

                    <Outlet />

                    <footer className='footer-nav-bar'>

                        <div className="footer-body">

                            <div className="footer-header">
                                <div className="footer-logo"></div>
                                <span className="footer-title">Land Of Peace</span>
                            </div>

                            <nav className="footer-nav">

                                <Link to="/about" className="footer-link about">About</Link>
                                <Link to="/help" className="footer-link help">Help</Link>
                                <Link to="/contact" className="footer-link contact">Contact</Link>
                                <Link to="/feedback" className="footer-link feedback">Feedback</Link>
                                <Link to="/donate" className="footer-link donate">Donate</Link>
                                <Link to="/support" className="footer-link support">Support</Link>
                                <Link to="/advertise" className="footer-link advertise">Advertise</Link>
                                <Link to="/partners" className="footer-link partners">Partners</Link>
                                <Link to="/careers" className="footer-link careers">Careers</Link>
                                <Link to="/developers" className="footer-link devs">Developers</Link>
                                <Link to="/investors" className="footer-link invest">Investors</Link>
                                <Link to="/press" className="footer-link press">Press</Link>
                                <Link to="/legal" className="footer-link legal">Legal</Link>
                                <Link to="/policies" className="footer-link policies">Policies</Link>
                                <Link to="/cookies" className="footer-link cookies">Cookies</Link>
                                <Link to="/ads" className="footer-link ads">Ads</Link>
                                <Link to="/more" className="footer-link more">More</Link>

                            </nav>

                        </div>

                        <div className="footer-footer">

                            <span className="footer-copy">© 2024 Land Of Peace</span>

                            <span className="footer-terms">
                                <Link to="/terms" className="footer-link terms">Terms</Link>
                                <Link to="/privacy" className="footer-link privacy">Privacy</Link>
                            </span>

                        </div>

                    </footer>

                </div>

            </section>

            <aside className='rigth-side-nav-bar'>
                <div className='rigth-side-nav'>
                    <span className='toggle-button'>
                        <span></span>
                        <span></span>
                        <span></span>
                    </span>
                    <div className='menu'>
                        <a href='#calendar' className='menu-link'>
                            <Calendar2Date size={20}/>
                            <span className="online">
                                <span className="online-dot"></span>
                            </span>
                        </a>
                        <a href='#notification' className='menu-link'>
                            <Bell size={20} />
                            <span className="online">
                                <span className="online-dot"></span>
                            </span>
                        </a>
                        <a href='#message' className='menu-link'>
                            <ChatLeft size={20} />
                            <span className="online">
                                <span className="online-dot"></span>
                            </span>
                        </a>
                        <a href='#friend' className='menu-link'>
                            <PersonCircle size={20} />
                            <span className="online">
                                <span className="online-dot"></span>
                            </span>
                        </a>
                    </div>
                </div>
            </aside>

        </main>
    )
}

export default Index
