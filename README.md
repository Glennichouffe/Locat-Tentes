# Locat-Tentes
    <record id="action_create_appointments" model="ir.actions.server">
        <field name="name">Create Appointment</field>
        <field name="model_id" ref="om_hospital.model_hospital_patient"/>
        <field name="binding_model_id" ref="om_hospital.model_hospital_patient"/>
        <field name="binding_view_types">list,form</field>
        <field name="state">code</field>
        <field name="code">
            if record:
                action_values = env.ref('om_hospital.action_create_appointment').sudo().read()[0]
                action_values.update({'context': env.context})
                action = action_values
        </field>
    </record>

    <record id="view_patient_kanban" model="ir.ui.view">
        <field name="name">hospital.patient.kanban</field>
        <field name="model">hospital.patient</field>
        <field name="arch" type="xml">
            <kanban default_order="id asc">
                <field name="id"/>
                <field name="name"/>
                <field name="reference"/>
                <field name="gender"/>
                <field name="age"/>
                <field name="note"/>
                <templates>
                    <t t-name="kanban-box">
                        <div t-attf-class="oe_kanban_global_click">
                            <div class="oe_kanban_details">
                                <ul>
                                    <li>
                                        ID: <field name="reference"/>
                                    </li>
                                    <li>
                                        Name: <field name="name"/>
                                    </li>
                                    <li>
                                        Age: <field name="age"/>
                                    </li>
                                    <li>
                                        Gender: <field name="gender"/>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </t>
                </templates>
            </kanban>
        </field>
    </record>

    <record id="view_patient_tree" model="ir.ui.view">
        <field name="name">hospital.patient.tree</field>
        <field name="model">hospital.patient</field>
        <field name="arch" type="xml">
            <tree>
                <field name="reference"/>
                <field name="name"/>
                <field name="responsible_id"/>
                <field name="gender"/>
                <field name="age"/>
                <field name="note"/>
                <field name="appointment_count"/>
<!--                <field name="state"/>-->
            </tree>
        </field>
    </record>

    <record id="view_patient_form" model="ir.ui.view">
        <field name="name">hospital.patient.form</field>
        <field name="model">hospital.patient</field>
        <field name="arch" type="xml">
            <form>
                <header>
<!--                    <button id="button_confirm" name="action_confirm" string="Confirm" class="btn-primary" states="draft"-->
<!--                            confirm="Are you sure that you need to confirm ?"-->
<!--                            type="object"/>-->
<!--                    <button id="button_done" name="action_done" string="Mark As Done" class="btn-primary" states="confirm"-->
<!--                            type="object"/>-->
<!--                    <button id="button_draft" name="action_draft" string="Set To Draft" class="btn-primary"-->
<!--                            states="cancel" type="object"/>-->
<!--                    <button id="button_cancel" name="action_cancel" string="Cancel" states="draft,done,confirm"-->
<!--                            confirm="Are you sure that you need to cancel ?"-->
<!--                            type="object"/>-->
<!--                    <button id="button_create_appointment" name="%(om_hospital.action_create_appointment)d"-->
<!--                            string="Create Appointment" class="btn-primary"-->
<!--                            type="action"/>-->
<!--                    <field name="state" widget="statusbar" statusbar_visible="draft,done,confirm"/>-->
                </header>
                <sheet>
                    <div class="oe_button_box" name="button_box">
                        <button name="action_open_appointments" type="object" class="oe_stat_button" icon="fa-calendar">
                            <div class="o_stat_info">
                                <field name="appointment_count" class="o_stat_value"/>
                                <span class="o_stat_text">Appointments</span>
                            </div>
                        </button>
                    </div>
                    <field name="image" widget="image" class="oe_avatar"/>
                    <div class="oe_title">
                        <h1>
                            <field name="reference" readonly="1"/>
                        </h1>
                    </div>
                    <group>
                        <group>
                            <field name="name"/>
                            <field name="responsible_id"/>
                            <field name="age"/>
                            <field name="appointment_count"/>
                        </group>
                        <group>
                            <field name="gender" invisible="context.get('hide_gender')"/>
                            <field name="note"/>
                        </group>
                    </group>
                    <notebook>
                        <page string="Appointments" name="appointment">
                            <field name="appointment_ids" readonly="1">
                            </field>
                        </page>
                    </notebook>
                </sheet>
                <div class="oe_chatter">
                    <field name="message_follower_ids"/>
                    <field name="activity_ids"/>
                    <field name="message_ids"/>
                </div>
            </form>
        </field>
    </record>

    <record id="view_patient_search" model="ir.ui.view">
        <field name="name">hospital.patient.search</field>
        <field name="model">hospital.patient</field>
        <field name="arch" type="xml">
            <search string="Patients">
                <field name="name"/>
                <field name="note"/>
                <separator/>
                <filter string="Male" name="male" domain="[('gender', '=', 'male')]"/>
                <filter string="Female" name="female" domain="[('gender', '=', 'female')]"/>
                <filter string="Others" name="other" domain="[('gender', '=', 'other')]"/>
                <group expand="1" string="Group By">
                    <filter string="Gender" name="gender" context="{'group_by':'gender'}"/>
                    <filter string="Patient Name" name="patient_name" context="{'group_by':'name'}"/>
                    <filter string="Responsible" name="responsible_id" context="{'group_by':'responsible_id'}"/>
                </group>
            </search>
        </field>
    </record>