import { useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { crearUsuario, eliminarUsuario, actualizarUsuario, obtenerUsuario } from '../api/usuario.api';
import { useNavigate, useParams } from 'react-router-dom';


export function UsuarioFormPage() {

    const {register, handleSubmit, setValue} = useForm();
    const navigate = useNavigate();
    const params = useParams();

    const onSubmit= handleSubmit(async (data) => {
        if (params.id){
            await actualizarUsuario(params.id, data);
            //console.log('actualixando');
        } else {
            await crearUsuario(data);
        }
        navigate('/usuario');
    })

    useEffect(() => {
        async function cargarUsuario(){
            if (params.id){
                const res = await obtenerUsuario(params.id);
                console.log(res);
                setValue('nombre', res.data.user.nombre)
                setValue('email', res.data.user.email)
                setValue('edad', res.data.user.edad)
            }
        } 
        cargarUsuario();
    }, [])

    return (
        <>
            <div className="container-fluid contenedor-login bg-light d-flex justify-content-center align-items-center vh-100">
                <div className="bg-white p-5 rounded-3 text-secondary shadow productForm-box">
                    <p className="text-center fs-3 fw-bold">Crear Usuario</p>
                    <div className="row d-flex">
                        <div className="col">
                            <div className="overflow-auto div-overflow">
                                <form onSubmit={onSubmit}>
                                    <div className="mb-3">
                                        <label htmlFor="nombre" className="form-label">Nombre</label>
                                        <input type="text" className="form-control" id="nombre" aria-describedby="emailHelp"
                                            {...register("nombre", {required: true})}
                                        />
                                    </div>
                                    <div className="mb-3">
                                        <label htmlFor="email" className="form-label">Email</label>
                                        <input type="email" className="form-control" id="email" aria-describedby="emailHelp"
                                            {...register("email", {required: true})}
                                        />
                                    </div>
                                    <div className="mb-3">
                                        <label htmlFor="edad" className="form-label">Edad</label>
                                        <input type="number" className="form-control" id="edad"
                                            {...register("edad")}
                                        />
                                    </div>
                                    <button type="submit" className="btn btn-primary">Guardar</button>
                                </form>

                                {
                                    params.id && (<button className='btn btn-danger p-2 my-3' onClick={ async () => {
                                        const acepta = window.confirm('estas seguro de eliminar este usuario?')
                                        if (acepta){
                                            await eliminarUsuario(params.id);
                                            navigate('/usuario');
                                        }
                                    }}>Delete</button>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}