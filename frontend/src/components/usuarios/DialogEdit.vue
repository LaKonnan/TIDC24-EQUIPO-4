<template>
    <div>
        <b-modal id="modal-xle" size="xl" title="EDITAR OBRA" hide-footer>
            <hr>
            <b>Usuario:</b>
            <b-col>
                <b-row>Fecha de creación: {{items[0].created_at}}</b-row>
                <b-row>Nombre: {{items[0].nickname}}</b-row>
                <b-row>Email: {{items[0].email}}</b-row>
            </b-col>
            <hr>
            <b-form @submit.stop.prevent="onSubmit">
                <b-form-group id="input-group-1" label="Nombre" label-for="input-1">
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

                <b-form-group id="input-group-2" label="Email" label-for="input-2">
                <b-form-input
                    id="input-2"
                    name="input-2"
                    type="text"
                    v-model="$v.form.email.$model"
                    :state="validateState('email')"
                    aria-describedby="input-2-live-feedback"
                ></b-form-input>
                <b-form-invalid-feedback
                    id="input-2-live-feedback"
                >Este es un campo obligatorio y requiere un email válido.</b-form-invalid-feedback>
                </b-form-group>

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
                >Este es un campo obligatorio y requiere un mínimo de 6 carácteres.</b-form-invalid-feedback>
                </b-form-group>

                <b-button type="submit" class="normal-button">Editar</b-button>
                <b-button class="dark-button" @click="resetForm()">Limpiar Campos</b-button>
            </b-form>  
        </b-modal>
    </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, minLength, email } from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],
  props: ['items'],
  data() {
    return {
      form: {
        name: null,
        email: null,
        password: null
      }
    };
  },
  validations: {
    form: {
      name: {
        required,
        minLength: minLength(3)
      },
      email: {
        email,
        required
      },
      password: {
        required,
        minLength: minLength(6)
      }
    }
  },
  methods: {
    validateState(name) {
      const { $dirty, $error } = this.$v.form[name];
      return $dirty ? !$error : null;
    },
    resetForm() {
      this.form = {
        name: null,
        email: null,
        password: null
      };

      this.$nextTick(() => {
        this.$v.$reset();
      });
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
