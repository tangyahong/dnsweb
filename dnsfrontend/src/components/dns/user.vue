<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right" style="font-size: 14px">
      <el-breadcrumb-item :to="{ path: '/dashboard' }"><i class="el-icon-menu"></i> 首页</el-breadcrumb-item>
      <el-breadcrumb-item>用户管理</el-breadcrumb-item>
    </el-breadcrumb>

    <div class="handle-box">
      <el-form :model="formFilter" ref="formFilter" style="display:inline-block">
        <el-row :gutter="10">

          <el-col class="handle-select-username">
            <el-form-item prop="input_username">
              <el-input placeholder="用户名"  size="small" v-model="formFilter.input_username" clearable></el-input>
            </el-form-item>
          </el-col>

          <el-col :span="1.5">
            <el-form-item>
              <el-button type="primary" icon="el-icon-search" size="small" @click="DataFilter()" :disabled='buttonDisabled'>{{ buttonDisabled | buttonFilter}}</el-button>
            </el-form-item>
          </el-col>

          <el-col :span="1.5">
            <el-form-item>
              <!-- <el-button type="success" icon="el-icon-circle-plus-outline" size="small" @click="addUser" :disabled='buttonDisabled'>新增</el-button> -->
              <el-button type="success" @click="addUser" :disabled='buttonDisabled' size="small"><icon name="add" scale="1.5" style="margin-top:-2px; float:left; padding-top:1px; padding-right:5px" ></icon>新增</el-button>
            </el-form-item>
          </el-col>

        </el-row>
      </el-form>
    </div>

    <el-table
        :data="data.slice((currentPage-1)*pageSize,currentPage*pageSize)"
        border
        style="width: 100%;"
        ref="multipleTable"
        size="mini">
      <el-table-column prop="username" label="用户名" align="center">
      </el-table-column>
      <el-table-column prop="role" label="角色" align="center">
      </el-table-column>
      <el-table-column prop="department" label="部门" align="center">
      </el-table-column>
      <el-table-column prop="name" label="姓名" align="center">
      </el-table-column>
      <el-table-column prop="login_time" label="登陆时间" align="center" width="220">
      </el-table-column>
      <el-table-column label="操作" align="center">
        <template slot-scope="scope">
          <el-button size="mini" type="text" @click="EditUser(scope.row)">
            <icon name="edit" scale="1.5" style="margin-top:-2px; float:left; padding-top:1px"></icon>编辑</el-button>
          <el-button size="mini" type="text" @click="resetPassword(scope.row)">
            <icon name="resetpassword" scale="1.5" style="margin-top:-2px; float:left; padding-top:1px"></icon><span>重置密码</span>
          </el-button>
          <!-- <el-button size="mini" type="warning" @click="ChangePassword(scope.row)" round>修改密码</el-button> -->
          <el-button size="mini" type="text" @click="deleteUser(scope.row)">
            <icon name="del" scale="1.5" style="margin-top:-2px; float:left; padding-top:1px"></icon><span>删除</span>
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog title="新增用户" :visible.sync="dialogFormVisible">
      <el-row :gutter="10">
        <el-col :sm="24" :md="24" :lg="12">
          <el-form ref="addForm" :model="addForm" label-width="80px" :rules="addRules">
            <el-form-item label="用户名" prop="username">
              <el-input v-model="addForm.username" size="small"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input v-model="addForm.password" size="small" type="password"></el-input>
            </el-form-item>
            <el-form-item label="姓名" prop="name">
              <el-input v-model="addForm.name" size="small"></el-input>
            </el-form-item>
            <el-form-item label="部门" prop="department">
              <el-input v-model="addForm.department" size="small"></el-input>
            </el-form-item>
            <el-form-item label="角色" prop="role">
              <el-select v-model="addForm.role" size="small" style="width:100%">
                <el-option label="管理员" value="管理员"></el-option>
                <el-option label="用户" value="用户"></el-option>
              </el-select>
            </el-form-item>
          </el-form>
        </el-col>
        <el-col :sm="24" :md="24" :lg="12">
          <div style="text-align:center">
            <el-tree
              :data="data2"
              show-checkbox
              node-key="id"
              ref="tree"
              style="height: 284px; overflow-y: auto"
              :default-expand-all=true
              :default-checked-keys=default_keys
              :props="defaultProps">
            </el-tree>
          </div>
        </el-col>
      </el-row>
      <el-row>
        <div style="text-align:center;">
          <el-button type="primary" @click="onSubmit" size="small">立即创建</el-button>
          <el-button size="small" @click="cancelForm()">取消</el-button>
        </div>
      </el-row>
    </el-dialog>

    <el-dialog title="编辑用户" :visible.sync="dialogEditFormVisible">
      <el-row :gutter="10">
        <el-col :sm="24" :md="24" :lg="12">
          <el-form ref="editForm" :model="editForm" label-width="80px" :rules="addRules">
            <el-form-item label="用户名" prop="username">
              <el-input v-model="editForm.username" size="small" disabled></el-input>
            </el-form-item>
            <el-form-item label="姓名" prop="name">
              <el-input v-model="editForm.name" size="small"></el-input>
            </el-form-item>
            <el-form-item label="部门" prop="department">
              <el-input v-model="editForm.department" size="small"></el-input>
            </el-form-item>
            <el-form-item label="角色" prop="role">
              <el-select v-model="editForm.role" size="small" style="width:100%">
                <el-option label="管理员" value="管理员"></el-option>
                <el-option label="用户" value="用户"></el-option>
              </el-select>
            </el-form-item>
          </el-form>
        </el-col>
        <el-col :sm="24" :md="24" :lg="12">
          <div style="text-align:center">
            <el-tree
              :data="data2"
              show-checkbox
              node-key="id"
              ref="treeEdit"
              style="height:220px; overflow-y: auto"
              :default-expand-all=true
              :default-checked-keys=default_keys
              :props="defaultProps">
            </el-tree>
          </div>
        </el-col>
      </el-row>
      <el-row>
        <div style="text-align:center;">
          <el-button type="primary" @click="onEditSubmit" size="small">确定</el-button>
          <el-button size="small" @click="dialogEditFormVisible=false">取消</el-button>
        </div>
      </el-row>
    </el-dialog>

    <el-dialog title="修改密码" :visible.sync="dialogChangePasswordFormVisible"  width="40%">
      <el-row :gutter="10">
        <el-col :sm="24" :md="24" :lg="24">
          <el-form ref="changePasswordForm" :model="changePasswordForm" label-width="80px" :rules="changePasswordRules">
            <el-form-item label="旧密码" prop="oldPassword">
              <el-input v-model="changePasswordForm.oldPassword" size="small" type="password"></el-input>
            </el-form-item>
            <el-form-item label="新密码" prop="newPassword">
              <el-input v-model="changePasswordForm.newPassword" size="small" type="password"></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="confirmPassword">
              <el-input v-model="changePasswordForm.confirmPassword" size="small" type="password"></el-input>
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
      <el-row>
        <div style="text-align:center;">
          <el-button type="primary" @click="onChangePasswordSubmit" size="small">确定</el-button>
          <el-button size="small" @click="cancelChangePasswordForm">取消</el-button>
        </div>
      </el-row>
    </el-dialog>


    <div class="pagination" style="float: right; margin-top:10px">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        layout="total, sizes, prev, pager, next, jumper"
        :page-sizes="[5, 10, 20, 50]"
        :page-size="pageSize"
        :total="data.length">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  import { restful_path } from '../util.js'
  export default {
    data() {
      return {
        data: [],
        items: [],
        currentPage:1,
        pageSize:50,
        formFilter: {
          input_username: ''
        },
        buttonDisabled: false,
        dialogFormVisible: false,
        dialogEditFormVisible: false,
        dialogChangePasswordFormVisible: false,
        formLabelWidth:80,
        addForm: {
          username:'',
          password:'',
          department:'',
          name:'',
          role:''
        },
        editForm: {
          username:'',
          password:'',
          department:'',
          name:'',
          role:''
        },
        changePasswordForm: {
          oldPassword:'',
          newPassword:'',
          confirmPassword:''
        },
        default_keys:[],
        //default_keys_edit:[],
        addRules:{
          username:[{ required: true, message: '请输入用户名' }],
          name:[{ required: true, message: '请输入姓名' }],
          password:[{ required: true, message: '请输入密码'}],
          role:[{ required: true, message: '请选择角色'}],
          department:[{ required: true, message: '请输入部门名称'}]
        },
        changePasswordRules: {
          oldPassword:[{ required: true, message: '请输入旧密码' }],
          newPassword:[{ required: true, message: '请输入新密码' }],
          confirmPassword:[{ required: true, message: '请确认新密码' }]
        },
        data2: [{
          id: 1,
          label: 'Dashboard'
        }, {
          id: 2,
          label: 'TOPN域名分析'
        }, {
          id: 3,
          label: '资源分布分析'
        }, {
          id: 4,
          label: 'CDN分析'
        }, {
          id: 5,
          label: '重点行业分析'
        }, {
          label: '重点域名分析',
          children: [{
            id: 6,
            label: '重点域名展示'
          }, {
            id: 7,
            label: '重点域名管理'
          }]
        },{
          label: '多维度查询',
          children: [{
            id: 8,
            label: 'IP地址反查'
          }, {
            id: 9,
            label: '备案信息查询'
          }]
        },{
          label: '专线用户分析',
          children: [{
            id: 10,
            label: '专线用户管理'
          }, {
            id: 11,
            label: '专线用户画像'
          }]
        }, {
          id: 12,
          label: '大屏展示'
        },{
          id: 13,
          label: '用户管理'
        }],
        defaultProps: {
          children: 'children',
          label: 'label'
        }
      }
    },
    created() {
      //this.setStyle()
    },
    mounted() {
      //this.setStyle()
    },
    filters: {
      buttonFilter(status) {
        const statusMap = {
          true:'查询中',
          false:'查询'
        }
        return statusMap[status]
      },
      roleFilter(status) {
        const statusMap = {
          '0':'管理员',
          '1':'用户'
        }
        return statusMap[status]
      }
    },
    computed: {
    },
    methods: {
      handleSizeChange(size) {
       this.pageSize = size;
      },

      handleCurrentChange(currentPage) {
        this.currentPage = currentPage;
      },

      DataFilter() {
        this.buttonDisabled = true;
        this.$http({
          method: 'post',
          url: restful_path + '/api/get-user',
          data: {
            'username': this.formFilter.input_username,
          }
        }).then(response => {
          this.buttonDisabled = false;
          if (response.data.status){
            this.data = response.data.data;
          } else {
            this.data = [];
          }
        }).catch(error => {
          //console.log(error);
        });
      },

      addUser() {
        this.dialogFormVisible = true;
        this.$refs.addForm.resetFields();
      },

      deleteUser(row) {
        this.$confirm('是否删除用户？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
        }).then(() => {
          this.$http({
            method: 'post',
            url: restful_path + '/api/del-user',
            data: { 'id': row.id }
          }).then((response) => {
            if(response.data.status) {
              this.$message({type:'success', message:'删除成功！'});
              setTimeout(() => { this.DataFilter() }, 100);
            } else {
              this.$message({type:'error', message:'删除失败！'})
            }
          }).catch(error => {});
        })
      },

      resetPassword(row) {
        this.$confirm('是否重置密码？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
        }).then(() => {
          this.$http({
            method: 'post',
            url: restful_path + '/api/reset-password',
            data: { 'id': row.id }
          }).then((response) => {
            if(response.data.status) {
              this.$message({type:'success', message:'重置密码成功！'});
            } else {
              this.$message({type:'error', message:'重置密码失败！'})
            }
          }).catch(error => {});
        })
      },

      EditUser(row) {
        this.dialogEditFormVisible = true;
        this.editForm = Object.assign({}, row);
        this.$http({
          method: 'post',
          url: restful_path + '/api/get-privilege',
          data: {'id': row.id }
        }).then((response) => {
          this.$refs.treeEdit.setCheckedKeys(response.data.data);
        }).catch(error => {});
      },

      onSubmit() {
        this.$refs.addForm.validate((valid) => {
          if(valid){
            let crypto = require('crypto');
            let password = this.addForm.password;
            let password_hash = crypto.createHash('sha1').update(password).digest('hex');
            this.$http({
              method: 'post',
              url: restful_path + '/api/add-user',
              data: {
                'username': this.addForm.username,
                'password': password_hash,
                'name': this.addForm.name,
                'department': this.addForm.department,
                'role': this.addForm.role,
                'privilege': this.$refs.tree.getCheckedKeys()
              }
            }).then(response => {
              //this.buttonDisabled = false;
              if (response.data.status){
                this.$message({ type: 'success', message: '添加用户成功!' });
              } else {
                this.$message({ type: 'error', message: '添加用户失败!' });
              }
              this.$refs.addForm.resetFields();
              this.default_keys = [];
              this.dialogFormVisible = false;
              setTimeout(() => { this.DataFilter() }, 100);
            }).catch(error => {
              //console.log(error);
            });
          }
        })
      },

      onEditSubmit() {
        let para = Object.assign({}, this.editForm);
        this.$refs.editForm.validate((valid) => {
          if(valid){
            this.$http({
              method: 'post',
              url: restful_path + '/api/edit-user/' + para.id,
              data: {
                'name': para.name,
                'role': para.role,
                'department': para.department,
                'privilege': this.$refs.treeEdit.getCheckedKeys()
              }
            }).then((response) => {
              if (response.data.status){
                this.$message({ type: 'success', message: '修改用户成功!' });
              } else {
                this.$message({ type: 'error', message: '修改用户失败!' });
              }
              this.dialogEditFormVisible = false;
              setTimeout(() => { this.DataFilter() }, 100);
            }).catch(error => {
              //console.log(error);
            });
          }
        })
      },

      ChangePassword(row) {
        this.dialogChangePasswordFormVisible = true;
        this.changePasswordForm = Object.assign({}, row);
      },

      onChangePasswordSubmit() {
        this.$refs.changePasswordForm.validate((valid) => {
          if(valid){
            let para = Object.assign({}, this.changePasswordForm);
            let crypto = require('crypto');
            let oldPassword = this.changePasswordForm.oldPassword;
            let old_password_hash = crypto.createHash('sha1').update(oldPassword).digest('hex');
            let newPassword = this.changePasswordForm.newPassword;
            let new_password_hash = crypto.createHash('sha1').update(newPassword).digest('hex');
            let confirmPassword = this.changePasswordForm.confirmPassword;
            let confirm_password_hash = crypto.createHash('sha1').update(confirmPassword).digest('hex');
            this.$http({
              method: 'post',
              url: restful_path + '/api/change-password',
              data: {
                'id': para.id,
                'oldPassword': old_password_hash,
                'newPassword': new_password_hash,
                'confirmPassword': confirm_password_hash
              }
            }).then((response) => {
              if (response.data.status){
                this.$message({ type: 'success', message: '修改密码成功!' });
                this.dialogChangePasswordFormVisible = false;
                this.$refs.changePasswordForm.resetFields();
              } else {
                if(response.data.data != ""){
                  this.$message({ type: 'error', message: response.data.data });
                } else {
                  this.$message({ type: 'error', message: '修改密码失败!' });
                }
              }
            }).catch(error => {
              //console.log(error);
            });
          }
        })
      },

      cancelForm(){
        this.dialogFormVisible = false;
        this.$refs.addForm.resetFields();
      },

      cancelChangePasswordForm() {
        this.dialogChangePasswordFormVisible = false;
        this.$refs.changePasswordForm.resetFields();
      }
    }
  }
</script>

<style lang="scss" scoped>
  .handle-box{
    margin-top: 20px;
    text-align: center;
  }
  .handle-select-username {
    width: 200px;
  }
</style>