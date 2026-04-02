/** @odoo-module **/
import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { user } from "@web/core/user";
import { useService } from "@web/core/utils/hooks";

export class TodoItem extends Component {
    static template = "HelloWorld.TodoItem";

    setup() {
        // useService - hook que permite acceder a los servicios de Odoo, ORM para interactuar con la base de datos
        this.orm = useService("orm");
        this.actionService = useService("action");
        // useState - hook que permite gestionar el estado del componente, se inicializa con un objeto que contiene X info.
        // es llamado en el xml
        this.state = useState({
            username: user.name,
            status: "Panel de Control",
            records: [],
            draftCount: 0,
            lockedCount: 0,
        });
        // onWillStart se ejecuta antes de que el componente se muestre
        onWillStart(async () => {
            await this.loadData();
        });
    }

    async openRecord(recordId) {
    this.state.status = "Abriendo formulario...";
    await this.actionService.doAction({
        type: 'ir.actions.act_window',
        res_model: 'sh.hello.world',
        res_id: recordId,
        views: [[false, 'form']],
        target: 'current',
    });
    }

    async loadData() {
        // searchRead es un método del servicio ORM que permite buscar y leer registros de un modelo
        const data = await this.orm.searchRead("sh.hello.world", [], ["name", "state"]);
        this.state.records = data;
        this.state.draftCount = data.filter(r => r.state === 'draft').length;
        this.state.lockedCount = data.filter(r => r.state === 'locked').length;
    }

    async deleteRecord(recordId) {
        // Borramos en la base de datos
        await this.orm.unlink("sh.hello.world", [recordId]);
        // Actualizamos la interfaz filtrando el array
        await this.loadData();
        this.state.status = "Registro eliminado";

    }

    finishTask() {
        this.loadData(); // Refrescar datos
        this.state.status = "Datos Actualizados";
    }
}

// - método que permite registrar el componente en una categoría específica, 
// en este caso "actions", con un nombre único "hello_world.todo_action"
registry.category("actions").add("hello_world.todo_action", TodoItem);