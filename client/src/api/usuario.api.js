import axios from 'axios'

const usuarioApi = axios.create({
    baseURL: "http://127.0.0.1:8000/api/usuarios/",
})
export const getUsuarios = () => usuarioApi.get("/");
export const crearUsuario = (usuario) => usuarioApi.post("/", usuario);

export const eliminarUsuario = (id) => usuarioApi.delete(`/${id}`);
export const actualizarUsuario = (id, usuario) => usuarioApi.put(`/${id}/`, usuario);

export const obtenerUsuario = (id) => usuarioApi.get(`/${id}`)

