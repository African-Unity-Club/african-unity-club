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

import { Link, Outlet, useParams } from 'react-router-dom';
import '../style/All.css'


function Index() {

    const username = 'unknown'

    return (
        <main className="index-main">

            <aside className="left-side-nav-bar">
                
                <div className="side-nav-bar-header">
                    <div className="userlogo">
                        <img src="./noprofile.jpeg" alt="userlogo" className="userlogo-img" />
                        <span className="online"></span>
                    </div>
                    <span className="username">{username}</span>
                </div>

                <nav className="side-body">
                    <Link to={`/dashboard/${username}`} className="sidenav-link">
                        <GraphDownArrow size={20} />
                        Dashboard
                    </Link>
                    <Link to={`/profile/${username}`} className="sidenav-link">
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
                    <Link to={`/settings/${username}`} className="sidenav-link">
                        <Sliders size={20}/>
                        Settings</Link>
                </nav>

                <div className="side-footer">
                    <Link to="/logout" className="sidenav-link">
                        <ArrowLeftCircle size={20} />
                        Logout
                    </Link>
                </div>

            </aside>

            <section className='body-content'>

                <header className='header-content-nav-bar'>

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

                            <Link to={`/calendar/${username}`} className="header-link">
                                <Calendar2Date size={20} />
                            </Link>

                            <Link to={`/notification/${username}`} className="header-link">
                                <Bell size={20} />
                                <span className='total'>104</span>
                            </Link>

                            <Link to={`/message/${username}`} className="header-link">
                                <ChatLeft size={20} />
                                <span className='total'>104</span>
                            </Link>

                            <Link to={`/friendish/${username}`} className="header-link">
                                <PersonCircle size={20} />
                                <span className='total'>104</span>
                            </Link>

                        </nav>

                    </div>

                </header>

                <Outlet />

                <footer className='footer-nav-bar'>

                    <div className="footer-body">

                        <div className="footer-header">
                            <div className="footer-logo">
                                <span className="logo"></span>
                            </div>
                            <span className="footer-title">Dream Africa</span>
                        </div>

                        <nav className="footer-nav">

                            <Link to="/about" className="footer-link">About</Link>
                            <Link to="/help" className="footer-link">Help</Link>
                            <Link to="/contact" className="footer-link">Contact</Link>
                            <Link to="/feedback" className="footer-link">Feedback</Link>
                            <Link to="/donate" className="footer-link">Donate</Link>
                            <Link to="/support" className="footer-link">Support</Link>
                            <Link to="/advertise" className="footer-link">Advertise</Link>
                            <Link to="/partners" className="footer-link">Partners</Link>
                            <Link to="/careers" className="footer-link">Careers</Link>
                            <Link to="/developers" className="footer-link">Developers</Link>
                            <Link to="/investors" className="footer-link">Investors</Link>
                            <Link to="/press" className="footer-link">Press</Link>
                            <Link to="/legal" className="footer-link">Legal</Link>
                            <Link to="/policies" className="footer-link">Policies</Link>
                            <Link to="/cookies" className="footer-link">Cookies</Link>
                            <Link to="/ads" className="footer-link">Ads</Link>
                            <Link to="/more" className="footer-link">More</Link>

                        </nav>

                    </div>

                    <div className="footer-footer">

                        <span className="footer-copy">© 2024 Dream Africa</span>

                        <span className="footer-terms">
                            <Link to="/terms" className="footer-link">Terms</Link>
                            <Link to="/privacy" className="footer-link">Privacy</Link>
                        </span>

                    </div>

                </footer>

            </section>

        </main>
    )
}

export default Index
