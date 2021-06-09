<template>
    <div>
        <b-modal id="modal-xlc" size="xl" title="NUEVA OBRA" hide-footer>
            <b-form @submit.stop.prevent="onSubmit">
            <b-form-group id="input-group-1" label="Encargado" label-for="input-1">
              <b-form-input
                id="input-1"
                name="input-1"
                v-model="$v.form.name.$model"
                :state="validateState('name')"
                aria-describedby="input-1-live-feedback"
              ></b-form-input>
              <b-form-invalid-feedback
                id="input-1-live-feedback"
              >Este es un campo obligatorio y requiere un mínimo de 3 carácteres.</b-form-invalid-feedback>
            </b-form-group>

            <b-form-group id="input-group-2" label="Nombre" label-for="input-2">
              <b-form-input
                id="input-2"
                name="input-2"
                type="text"
                v-model="$v.form.name1.$model"
                 :state="validateState1('name1')"
                aria-describedby="input-2-live-feedback"
              ></b-form-input>
              <b-form-invalid-feedback
                id="input-2-live-feedback"
              >Este es un campo obligatorio y requiere un mínimo de 3 carácteres.</b-form-invalid-feedback>
            </b-form-group>

             <b-form-group id="input-group-3" label="Estado" label-for="input-3">
                <b-form-select
                    id="input-3"
                    name="input-3"
                    v-model="selected1" 
                    :options="options1"
                    required
                ></b-form-select>
                </b-form-group>

                 <b-form-group id="input-group-4" label="Tipo" label-for="input-4">
                <b-form-select
                    id="input-4"
                    name="input-4"
                    type="select"
                    v-model="selected2" 
                    :options="options2"
                    required
                ></b-form-select>
                </b-form-group>
            <b-button type="submit" class="normal-button">Crear obra</b-button>
          </b-form>
        </b-modal>
    </div>
</template>

<script>

import { validationMixin } from "vuelidate";
import { required, minLength,} from "vuelidate/lib/validators";


export default {
    mixins: [validationMixin],
  data() {
    return {
      options1: [
                { value: 'Activa', text: 'Activa'},
                { value: 'Inactiva', text: 'Inactiva'},
                { value: 'Finalizada', text: 'Finalizada' }
            ],
             options2: [
                { value: 'Obra', text: 'Obra'},
                { value: 'Gerencia', text: 'Gerencia'},
                { value: 'Oficina', text: 'Oficina'}
            ],
      form: {
        name: null,
        name1: null,
        selected1: null,
        selected2: null
      }
    };
  },
  validations: {
    form: {
       name: {
        required,
        minLength: minLength(3)
      },
      name1: {
        required,
        minLength: minLength(3)
      },

      
    }
  },
  methods: {
    validateState(name) {
      const { $dirty, $error } = this.$v.form[name];
      return $dirty ? !$error : null;
    },

     validateState1(name1) {
      const { $dirty, $error } = this.$v.form[name1];
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

