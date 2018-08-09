<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right" style="font-size: 14px">
      <el-breadcrumb-item :to="{ path: '/index' }"><i class="el-icon-menu"></i> 首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/usermanage' }">用户管理</el-breadcrumb-item>
      <el-breadcrumb-item>账号管理</el-breadcrumb-item>
    </el-breadcrumb>

    <div class="handle-box">

      <el-form :model="formFilter" ref="formFilter">
        <el-row :gutter="10">
          <el-col :span="3">
            <el-form-item prop="select_city">
              <el-select placeholder="部门"  size="small" v-model="formFilter.select_city">
                <el-option key="1" label="省NOC" value="省NOC"></el-option>
              </el-select>
            </el-form-item>
          </el-col>

          <el-col :span="3">
            <el-form-item prop="select_isOccupied">
              <el-select placeholder="角色" size="small" v-model="formFilter.select_isOccupied">
                <el-option key="1" label="管理员" value="管理员" style="text-align: center;"></el-option>
                <el-option key="2" label="用户" value="用户" style="text-align: center;"></el-option>
              </el-select>
            </el-form-item>
          </el-col>

          <el-col :span="5">
            <el-form-item prop="input_ipAddress">
              <el-input placeholder="用户名"  size="small" v-model="formFilter.input_ipAddress"></el-input>
            </el-form-item>
          </el-col>

          <el-col :span="1.5">
            <el-form-item>
              <el-button type="primary" icon="el-icon-search" size="small" @click="DataFilter()">查询</el-button>
            </el-form-item>
          </el-col>

          <el-col :span="1.5">
            <el-form-item>
              <el-button type="warning" icon="el-icon-circle-plus-outline" size="small" @click="resetSearch('formFilter')">重置</el-button>
            </el-form-item>
          </el-col>

          <el-col :span="1.5">
            <el-form-item>
              <el-button type="success" icon="el-icon-circle-plus-outline" size="small" @click="dialogFormVisible = true">新增</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>

      <!-- 新增Form -->
      <el-dialog title="新增" :visible.sync="dialogFormVisible">
        <el-form :model="formAdd" :rules="formAddRules" ref="formAdd">
          <el-row>
            <el-col :span="8">
              <el-form-item label="地市" :label-width="formLabelWidth" prop="city">
                <el-select v-model="formAdd.city" placeholder="地市" size="small">
                  <el-option label="清远" value="清远"></el-option>
                  <el-option label="惠州" value="惠州"></el-option>
                  <el-option label="韶关" value="韶关"></el-option>
                  <el-option label="汕尾" value="汕尾"></el-option>
                  <el-option label="河源" value="河源"></el-option>
                  <el-option label="深圳" value="深圳"></el-option>
                </el-select>
              </el-form-item>
            </el-col>

            <el-col :span="8">
              <el-form-item label="地址类型" :label-width="formLabelWidth" prop="type">
                <el-select v-model="formAdd.type" placeholder="地址类型" size="small">
                  <el-option label="Loopback地址" value="Loopback地址"></el-option>
                  <el-option label="互联地址" value="互联地址"></el-option>
                </el-select>
              </el-form-item>
            </el-col>

            <el-col :span="8">
              <el-form-item label="占用状态" :label-width="formLabelWidth" prop="isOccupied">
                <el-select v-model="formAdd.isOccupied" placeholder="占用状态" size="small">
                  <el-option label="空闲" value="空闲"></el-option>
                  <el-option label="占用" value="占用"></el-option>
                </el-select>
              </el-form-item>
            </el-col>

          </el-row>
          </el-row>
            <el-col :span="24">
              <el-form-item label="IP地址段" :label-width="formLabelWidth" size="small" prop="ipAddress">
                <el-input v-model="formAdd.ipAddress" auto-complete="off"></el-input>
              </el-form-item>
            </el-col>
          </el-row>

        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancelForm('formAdd')" size="small">取 消</el-button>
          <el-button type="primary" @click="submitFormAdd('formAdd')" size="small">确 定</el-button>
        </div>
      </el-dialog>
    </div>

    <el-table
        :data="data.slice((currentPage-1)*pageSize,currentPage*pageSize)"
        border
        style="width: 100%; margin-top:20px;"
        ref="multipleTable"
        size="mini">
      <el-table-column type="selection" width="40" align="center">
      </el-table-column>
      <el-table-column prop="id" label="id" align="center" v-if="false">
      </el-table-column>
      <el-table-column prop="role" label="角色" width="100" align="center" >
      </el-table-column>
      <el-table-column prop="username" label="用户名" width="100" align="center">
      </el-table-column>
      <el-table-column prop="name" label="姓名" width="100" align="center" >
      </el-table-column>
      <el-table-column prop="department" label="部门" width="100" align="center" >
      </el-table-column>
      <el-table-column prop="email" label="邮箱" width="140" align="center">
      </el-table-column>
      <el-table-column prop="mobile" label="手机" width="140" align="center">
      </el-table-column>
      <el-table-column prop="login_time" label="登录时间" align="center" >
      </el-table-column>
      <el-table-column label="操作" width="240" align="center">
        <template slot-scope="scope">
          <el-button size="mini" type="info" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 编辑Form -->
    <el-dialog title="编辑" :visible.sync="dialogFormEditVisible">
      <el-form :model="formEdit" :rules="formEditRules" ref="formEdit">
        <el-row>
          <el-col :span="8">
            <el-form-item label="地市" :label-width="formLabelWidth" prop="city">
              <el-select v-model="formEdit.city" placeholder="地市" size="small">
                <el-option label="清远" value="清远"></el-option>
                <el-option label="惠州" value="惠州"></el-option>
                <el-option label="韶关" value="韶关"></el-option>
                <el-option label="汕尾" value="汕尾"></el-option>
                <el-option label="河源" value="河源"></el-option>
                <el-option label="深圳" value="深圳"></el-option>
              </el-select>
            </el-form-item>
          </el-col>

          <el-col :span="8">
            <el-form-item label="地址类型" :label-width="formLabelWidth" prop="type">
              <el-select v-model="formEdit.type" placeholder="地址类型" size="small">
                <el-option label="Loopback地址" value="Loopback地址"></el-option>
                <el-option label="互联地址" value="互联地址"></el-option>
              </el-select>
            </el-form-item>
          </el-col>

          <el-col :span="8">
            <el-form-item label="占用状态" :label-width="formLabelWidth" prop="isOccupied">
              <el-select v-model="formEdit.isOccupied" placeholder="占用状态" size="small">
                <el-option label="空闲" value="空闲"></el-option>
                <el-option label="占用" value="占用"></el-option>
              </el-select>
            </el-form-item>
          </el-col>

        </el-row>
        </el-row>
        <el-col :span="24">
          <el-form-item label="IP地址段" :label-width="formLabelWidth" size="small" prop="ipAddress">
            <el-input v-model="formEdit.ipAddress" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        </el-row>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="cancelForm('formEdit')" size="small">取 消</el-button>
        <el-button type="primary" @click="submitFormEdit('formEdit')" size="small">确 定</el-button>
      </div>
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

  export default {
    data() {
      var ipAddressAddValidator = (rule, value, callback) => {
        if(!value){
          return callback(new Error('IP地址不能为空'));
        }
        setTimeout(() => {
          if(!isValidIP(value, this.formAdd.type)){
            callback(new Error("IP地址不符合要求"));
          } else {
            callback();
          }
        }, 200);
      };

      var ipAddressEditValidator = (rule, value, callback) => {
        if(!value){
          return callback(new Error('IP地址不能为空'));
        }
        setTimeout(() => {
          if(!isValidIP(value, this.formEdit.type)){
            callback(new Error("IP地址不符合要求"));
          } else {
            callback();
          }
        }, 200);
      };

      return {
        data: [],
        currentPage:1,
        pageSize:10,
        dialogFormVisible: false,
        dialogFormEditVisible: false,

        formFilter: {
          select_city: '',
          select_isOccupied: '',
          input_ipAddress: '',
          select_type: ''
        },

        formAdd: {
          ipAddress: '',
          city: '',
          isOccupied:'',
          type:''
        },
        formEdit: {
          ipAddress: '',
          city: '',
          isOccupied:'',
          type:''
        },

        formAddRules:{
          city:[{
            required: true,
            message: '请选择地市',
            trigger: 'blur'
          }],
          type:[{
            required: true,
            message: '请选择地址类型',
            trigger: 'blur'
          }],
          isOccupied:[{
            required: true,
            message: '请选择是否占用',
            trigger: 'blur'
          }],
          ipAddress:[{
            validator: ipAddressAddValidator,
            trigger: 'blur'
          }]
        },
        formEditRules:{
          city:[{
            required: true,
            message: '请选择地市',
            trigger: 'blur'
          }],
          type:[{
            required: true,
            message: '请选择地址类型',
            trigger: 'blur'
          }],
          isOccupied:[{
            required: true,
            message: '请选择是否占用',
            trigger: 'blur'
          }],
          ipAddress:[{
            validator: ipAddressEditValidator,
            trigger: 'blur'
          }]
        },

        formLabelWidth: '80px',
        //loading: true
      }
    },

    created() {
      this.showData();
    },

    methods: {

      handleSizeChange(size) {
       this.pageSize = size;
      },

      handleCurrentChange(currentPage) {
        this.currentPage = currentPage;
      },

      showData() {
        let token = this.$store.state.authModule.token
        //this.loading = true;
        /*console.log(this.loading)*/
        this.$http({
          method: 'get',
          url: 'http://127.0.0.1:5000/api/alluser',
          headers: {'Authorization': token}
        }).then(response => {
          this.data = response.data.data;
          /*this.loading = false;*/
        }).catch(error => {
          console.log(error);
        });

      },

      DataFilter() {
        this.$http({
          method: 'post',
          url: 'http://127.0.0.1:5000/ipManage',
          data: {
            'action': 2,
            'city': this.formFilter.select_city,
            'ipAddress': this.formFilter.input_ipAddress,
            'isOccupied': this.formFilter.select_isOccupied,
            'type': this.formFilter.select_type
          }
        }).then(response => { 
          this.data = response.data;
        }).catch(error => {
          console.log(error);
        });
      },

      resetSearch(formName){
        this.$refs[formName].resetFields();
      },

      submitFormAdd(formName) {
        this.$refs[formName].validate((valid) => {
          if(valid){
            this.$http({
              method: 'post',
              url: 'http://127.0.0.1:5000/ipManage',
              data: {
                'action': 1,
                'city': this.formAdd.city,
                'ipAddress': this.formAdd.ipAddress,
                'isOccupied': this.formAdd.isOccupied,
                'type': this.formAdd.type
              }
            }).then(response => { console.log(response); }).catch(error => {
              console.log(error);
            });
            this.dialogFormVisible = false;
            this.$refs[formName].resetFields();
            setTimeout(() =>{
              this.$http.get('http://127.0.0.1:5000/ipManage')
                .then(response => {
                  this.data = response.data
                })
                .catch(error => {
                  console.log(error);
                })
            }, 100)
          }
        });
      },

      cancelForm(formName){
        this.dialogFormVisible = false;
        this.$refs[formName].resetFields();
      },

      handleModifyStatus(row, status) {
        let val;
        if(row['isOccupied'] === "空闲"){
          val = '占用';
        } else {
          val = '空闲'
        };
        this.$confirm('是否将该IP地址段标记为' + val + '?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$http({
            method: 'put',
            url: 'http://127.0.0.1:5000/ipManage/' + row['id'],
            data: {
              'city': row['city'],
              'ipAddress': row['ipAddress'],
              'isOccupied': status,
              'type': row['type']
            }
          }).then((response) => {
            if(response.data["msg"] === 0){
              row.isOccupied = status;
              this.$message({
                type: 'success',
                message: '标记成功!'
              });
            }
          }).catch(error => {console.log(error);});
        }).catch(() => {});
      },

      handleEdit(index, row) {
        this.dialogFormEditVisible = true;
        this.formEdit = Object.assign({}, row);
      },

      submitFormEdit(formName) {
        this.$refs[formName].validate((valid) => { if(valid) {
          let para = Object.assign({}, this.formEdit);
          this.$http({
              method: 'put',
              url: 'http://127.0.0.1:5000/ipManage/' + para.id,
              data: {
                'city': para.city,
                'ipAddress': para.ipAddress,
                'isOccupied': para.isOccupied,
                'type': para.type
              }
            }).then(response => { console.log(response); }).catch(error => {
              console.log(error);
            });
            this.dialogFormEditVisible = false;
            this.$refs[formName].resetFields();
            setTimeout(() =>{
              this.$http.get('http://127.0.0.1:5000/ipManage')
                .then(response => {
                  this.data = response.data
                })
                .catch(error => {
                  console.log(error);
                })
            }, 100)
          }
        });
      },

      handleDelete(row) {
        console.log(row['id']);
        this.$confirm('是否将该IP地址段删除?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$http({
            method: 'delete',
            url: 'http://127.0.0.1:5000/ipManage/' + row['id']
          }).then((response) => {
            if(response.data["msg"] === 0){
              this.$message({
                type: 'success',
                message: '删除成功!'
              });
              setTimeout(() =>{
                this.$http.get('http://127.0.0.1:5000/ipManage')
                  .then(response => {
                    this.data = response.data
                  })
                  .catch(error => {
                    console.log(error);
                  })
              }, 100)
            }
          }).catch(error => {console.log(error);});
        }).catch(() => {});
      }
    }
  }
</script>

<style lang="scss" scopd>
  .handle-box{
    margin-top: 20px;
  }
  .handle-select-1{
    width: 75px;
  }
  .handle-select-2{
    width: 100px;
  }

  .handle-input{
    width: 300px;
  }

  .el-select-dropdown__item {
    text-align: center;
  }

  .el-input__inner {
    margin-right: 10px;
  }
</style>