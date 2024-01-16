import react from 'react'


class Views extends react.Component {
    constructor(props) {
        super(props);
        this.state = {
            views: 0
        }
    }

    // componentDidMount() {
    //     fetch('/api/views')
    //         .then(res => res.json())
    //         .then(views => this.setState({ views }));
    // }

    render() {
        return (
            <main className='vwh'>
                <div className='logo'></div>
                <div className='x-larg title'>Dream Africa</div>
                <div className='container'></div>
                <div className='container'></div>
            </main>
        );
    }
}

export default Views
