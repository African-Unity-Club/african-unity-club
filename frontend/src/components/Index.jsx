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
    let online = 'online'

    return (
        <main className="index-main">

            <aside className="left-side-nav-bar">
                
                <div className="side-nav-bar-header">
                    <div className="userlogo">
                        <img src="./noprofile.jpeg" alt="" className="userlogo-img" />
                        <span className="online">
                            <span className="online-dot"></span>
                        </span>
                    </div>
                    <span className="username">
                        {username}
                        <small>{online}</small>
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

                    <div className="header-body">

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

                    </div>

                    <div className="header-footer">
                        
                        <div className='header-footer-head'>
                            <span className='toggle'>
                                <span></span>
                                <span></span>
                                <span></span>
                            </span>
                            <h1 className="header-title">{`Dashboard`}</h1>
                        </div>
                        

                        <nav className="header-footer-nav">

                            <Link to={`/calendar/${username}`} className="header-link calendar">
                                <Calendar2Date size={20} />
                            </Link>

                            <Link to={`/notification/${username}`} className="header-link notification">
                                <Bell size={20} />
                                <span className='total'>104</span>
                            </Link>

                            <Link to={`/message/${username}`} className="header-link message">
                                <ChatLeft size={20} />
                                <span className='total'>104</span>
                            </Link>

                            <Link to={`/friendish/${username}`} className="header-link friend">
                                <PersonCircle size={20} />
                                <span className='total'>104</span>
                            </Link>

                        </nav>

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

        </main>
    )
}

export default Index
