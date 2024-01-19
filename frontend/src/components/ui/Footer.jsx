import { Link } from "react-router-dom";



const Footer = () => {

    return (
        <footer className="footer">
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
                <div className="footer-footer">
                    <span className="footer-copy">© 2024 Dream Africa</span>
                    <span className="footer-terms">
                        <Link to="/terms" className="footer-link">Terms</Link>
                        <Link to="/privacy" className="footer-link">Privacy</Link>
                    </span>
                </div>
            </div>
        </footer>
    )
}

export default Footer
