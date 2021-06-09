<template>
    <div>
        <b-modal id="modal-xld" size="xl" title="ELIMINAR OBRA" hide-footer>
            
               Obra a eliminar:
            <br><br>
            <b-col>
                <b-row>ID: {{items[0].obraId.S}}</b-row>
                <b-row>Nombre: {{items[0].nombre.S}}</b-row>
                <b-row>Encargado: {{items[0].encargado.S}}</b-row>
                <b-row>Estado: {{items[0].estado.S}}</b-row>
            </b-col>
            <br><br>
            <center>
            <p><b>IMPORTANTE: </b>Una vez eliminada la obra no podrá ser recuperada</p>
            <p><b>Para confirmar la eliminación, por favor, ingrese su contraseña de administrador.</b></p></center>
           <b-form @submit.stop.prevent="onSubmit">
                <b-form-group id="input-group-3" label="Contraseña" label-for="input-3">
                <b-form-input
                    id="input-3"
                    name="input-3"
                    type="password"
                    v-model="$v.form.password.$model"
                    :state="validateState('password')"
                    aria-describedby="input-3-live-feedback"
                ></b-form-input>
                <b-form-invalid-feedback
                    id="input-3-live-feedback"
                >Este es un campo obligatorio, requiere ingresar una contraseña.</b-form-invalid-feedback>
                </b-form-group>

                <b-button type="submit" class="dark-button">Eliminar</b-button>
            </b-form>  
        </b-modal>
    </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required } from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],
  props: ['items'],
  data() {
    return {
      form: {
        password: null
      }
    };
  },
  validations: {
    form: {
      password: {
        required
      }
    }
  },
  methods: {
    validateState(name) {
      const { $dirty, $error } = this.$v.form[name];
      return $dirty ? !$error : null;
    },
    onSubmit() {
      this.$v.form.$touch();
      if (this.$v.form.$anyError) {
        return;
      }
    }
  }
};
</script>
 