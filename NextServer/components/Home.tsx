import Footer from "./admin/Footer";
import Layout from "./admin/Layout";
import Navbar from "./admin/Navbar";

const Home: React.FC = () =>{
    return (<>
    <table style={{ width: "1200px", height: "600px", margin: "0 auto", border: "1px solid black"}}>
        <thead style={{ height: "20%",  border: "1px solid black"}}>
            <tr >
                <td style={{ width: "100%", border: "1px solid black"}}>
                <Navbar/>
                </td>
            </tr>
        </thead>
        <tbody>
        <tr style={{ width: "20%",height: "70%",  border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
            <Layout/>
            </td>
        </tr>
        
        <tr style={{ width: "100%", height: "10%", border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
            <Footer/>
            </td>
        </tr>
        </tbody>
    </table>
    </>)
}

export default Home
