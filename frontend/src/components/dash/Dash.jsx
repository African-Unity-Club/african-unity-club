import Header from '../ui/Header';
import Footer from '../ui/Footer';
import SideNav from '../ui/SideNav';
import '../../style/Dash.css'


function Dash() {

    const data = {
        username: "Hydromel",
        seo: [
            {
                name: "Africa",
                icon: "fas fa-globe-africa"
            },
            {
                name: "Asia",
                icon: "fas fa-globe-asia"
            },
            {
                name: "Europe",
                icon: "fas fa-globe-europe"
            },
            {
                name: "North America",
                icon: "fas fa-globe-americas"
            },
            {
                name: "South America",
                icon: "fas fa-globe-americas"
            },
            {
                name: "Australia",
                icon: "fas fa-globe-asia"
            },
            {
                name: "Antarctica",
                icon: "fas fa-globe-asia"
            }
        ]
    }

    return (
        <main className="main dash">
            <SideNav  props={data} />
            <section className="section">
                <Header props={data} />
                <div className="body">
                    <div></div>
                    <Footer />
                </div>
            </section>
        </main>
    )
}

export default Dash
