/** @odoo-module **/
import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { user } from "@web/core/user";
import { useService } from "@web/core/utils/hooks";

export class TodoItem extends Component {
    static template = "HelloWorld.TodoItem";

    setup() {
        // useService - hook que permite acceder a los servicios de Odoo, ORM para interactuar con la base de datos
        const orm = useService("orm");
        // useState - hook que permite gestionar el estado del componente, se inicializa con un objeto que contiene X info.
        // es llamado en el xml
        this.state = useState({
            username: user.name,
            status: "Sincronizando...",
            colorClass: "bg-primary",
            totalRecords: 0,
            records: [],
        });
        // onWillStart se ejecuta antes de que el componente se muestre
        onWillStart(async () => {
            try {
                // searchRead es un método del servicio ORM que permite buscar y leer registros de un modelo
                const data = await orm.searchRead("sh.hello.world", [], ["name"], { limit: 10 });
                
                this.state.records = data;
                this.state.totalRecords = data.length;
                this.state.status = "Lista cargada";
            } catch (error) {
                console.error("Error ORM:", error);
                this.state.status = "Error de lectura";
            }
        });
    }

    finishTask() {
        this.state.status = "Vista Refrescada";
    }
}
// - método que permite registrar el componente en una categoría específica, 
// en este caso "actions", con un nombre único "hello_world.todo_action"
registry.category("actions").add("hello_world.todo_action", TodoItem);