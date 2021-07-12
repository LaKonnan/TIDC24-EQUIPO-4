<template>
    <div>
        <b-modal id="modal-xld" size="lg" title="ELIMINAR USUARIO" hide-footer @hidden="onHidden">
            <!-- Datos de usuario -->
            <b-col>
                <b-row>Rut: {{items[0].identities[0].user_id}}</b-row>
                <b-row>Nombre: {{items[0].nickname}}</b-row>
                <b-row>Email: {{items[0].email}}</b-row>
            </b-col>
            <br>

            <center>
              <p><b>IMPORTANTE: </b>Una vez eliminado el usuario no podrá ser recuperado</p>
              <p><b>Para confirmar la eliminación del usuario, por favor, ingrese {{items[0].email}}</b></p>
            </center>

            <b-form @submit.stop.prevent="onSubmit">
                <b-form-group id="input-group-3" label-for="input-3">
                  {{setvEmail(items[0].email)}}
                <b-form-input
                    id="input-3"
                    name="input-3"
                    type="email"
                    v-model="$v.form.email.$model"
                    :state="validateState('email')"
                    style="text-align: center;" 
                    @paste.prevent 
                    aria-describedby="input-3-live-feedback"
                ></b-form-input>
                <b-form-invalid-feedback
                    id="input-3-live-feedback"
                >Este es un campo obligatorio y requiere el email solicitado.</b-form-invalid-feedback>
                </b-form-group>

                <b-button type="submit" class="dark-button">Eliminar</b-button>
            </b-form>  
        </b-modal>
    </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, sameAs } from "vuelidate/lib/validators";
import { getAPI } from '../axios-api';

export default {
  mixins: [validationMixin],
  props: ['items','table'],
  data() {
    return {
      form: {
        email: null,
        vemail: null,
        resume: []
      }
    };
  },

  validations: {
    form: {
      email: {
        required,
        sameAsEmail: sameAs('vemail')
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
        email: null,
        vemail: null
      };

      this.$nextTick(() => {
        this.$v.$reset();
      });
    },

    setvEmail(vemail) {
      this.form.vemail = vemail;
    },

    async onSubmit() {
      this.$v.form.$touch();
      if (this.$v.form.$anyError) {
        return;
      }else {
        const accessToken = await this.$auth.getTokenSilently()
        getAPI.delete('/usuarios/'+this.items[0].user_id, {
            headers: {
                Authorization: `Bearer ${accessToken}`
            }
        })
        .then(response => {
          console.log(response.data)
          this.$root.$emit('bv::hide::modal','modal-xld')
          this.resetForm()
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
  },
};
</script>