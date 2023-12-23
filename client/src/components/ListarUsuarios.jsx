import { useEffect, useState } from "react"
import { getUsuarios } from "../api/usuario.api";
import { useNavigate } from "react-router-dom";

export function ListarUsuarios() {

    const [usuarios, setUsuarios] = useState([]);
    const navigate = useNavigate();

    // el useEffect se carga apenas carga la pagina el cual llama a la funcion 
    // cargarusuarios y posterior a eso llama el metodo get al backEnd
    useEffect(() => {
        async function cargarUsuarios() {
            const res = await getUsuarios()
            setUsuarios(res.data.users);
        }
        cargarUsuarios();
    }, []);

    return <div className="container w-75 my-4">
        <table className="table table-bordered">
            <thead className="table-primary">
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Nombre</th>
                    <th scope="col">Email</th>
                    <th scope="col">Edad</th>
                    <th scope="col">Opciones</th>
                </tr>
            </thead>
            <tbody>
                {usuarios.map(usuario => (
                    <tr key={usuario.id}>
                        <th scope="row">{usuario.id}</th>
                        <td>{usuario.nombre}</td>
                        <td>{usuario.email}</td>
                        <td>{usuario.edad}</td>
                        <td>
                            <button className="btn btn-outline-dark" onClick={() => {
                                navigate(`/usuario/${usuario.id}`)
                            }}>Eliminar - editar</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>;
}