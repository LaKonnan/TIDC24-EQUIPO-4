<template>
    <div>
        <b-modal id="modal-xlc" size="xl" title="REGISTRAR NUEVO USUARIO" hide-footer @hidden="onHidden">
          <b-form @submit.stop.prevent="onSubmit">

            <b-form-group id="input-group-0" label="Rut" label-for="input-0">
              <b-form-input
                id="input-0"
                name="input-0"
                v-model="$v.form.rut.$model"
                :state="validateState('rut')"
                aria-describedby="input-0-live-feedback"
              ></b-form-input>
              <b-form-invalid-feedback
                id="input-0-live-feedback"
              >Este es un campo obligatorio</b-form-invalid-feedback>
            </b-form-group>

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

            <b-form-group id="input-group-4" label="Rol" label-for="input-4">
              <b-form-select v-model="$v.form.rol.$model"
                :state="validateState('rol')" :options="options"></b-form-select>
              <b-form-invalid-feedback
                id="input-4-live-feedback"
              >Este es un campo obligatorio</b-form-invalid-feedback>
            </b-form-group>

            <b-button type="submit" class="normal-button">Registrar</b-button>
            <b-button class="dark-button" @click="resetForm()">Limpiar Campos</b-button>
          </b-form>
        </b-modal>
    </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, minLength, email } from "vuelidate/lib/validators";
import { getAPI } from '../axios-api';

export default {
  mixins: [validationMixin],
  props: ['table'],
  data() {
    return {
      form: {
        rut: null,
        name: null,
        email: null,
        password: null,
        rol: null
      },
      options: [
        { value: null, text: 'Seleccione un rol' },
        { value: 'rol_QB4JcKnGKpJS7NLv', text: 'Administrador' },
        { value: 'rol_OwLZBI7MTfexCXk4', text: 'Gerente' },
        { value: 'rol_gxkCaxtBYTRDeqlF', text: 'Residente' },
        { value: 'rol_mvuY1l6CQeimpXsw', text: 'Encargado' },
      ]
    };
  },
  validations: {
    form: {
      rut: {
        required
      },
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
      },
      rol: {
        required
      }
    }
  },
  methods: {
    onHidden() {
      console.log('modal cerrado')
      this.table.get_users()
    },
    validateState(name) {
      const { $dirty, $error } = this.$v.form[name];
      return $dirty ? !$error : null;
    },
    resetForm() {
      this.form = {
        rut: null,
        name: null,
        email: null,
        password: null,
        rol: null
      };

      this.$nextTick(() => {
        this.$v.$reset();
      });
    },
    async onSubmit() {
      this.$v.form.$touch();
      if (this.$v.form.$anyError) {
        return;
      }else {
        const accessToken = await this.$auth.getTokenSilently()
        console.log(this.$v.form.rol.$model)
        getAPI.post('/usuarios', {
            rut: this.$v.form.rut.$model,
            name: this.$v.form.name.$model,
            email: this.$v.form.email.$model,
            password: this.$v.form.password.$model,
            rol: this.$v.form.rol.$model
        }, {
          headers: {
                Authorization: `Bearer ${accessToken}`
            }
        })
        .then(response => {
          console.log(response.data)
          this.$root.$emit('bv::hide::modal','modal-xlc')
          this.resetForm()
        })
        .catch(err => {
          console.log(err)
        })
      }
    }
  }
};
</script>
