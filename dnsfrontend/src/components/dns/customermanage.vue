<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right" style="font-size: 14px">
      <el-breadcrumb-item :to="{ path: '/dns-dashboard' }"><i class="el-icon-menu"></i> 首页</el-breadcrumb-item>
      <!-- <el-breadcrumb-item :to="{ path: '/dns-dashboard' }">DNS日志分析</el-breadcrumb-item> -->
      <el-breadcrumb-item>专线用户管理</el-breadcrumb-item>
    </el-breadcrumb>

    <div class="handle-box">
      <el-form :model="formFilter" ref="formFilter" style="display:inline-block">
        <el-row :gutter="10">
          <el-col :span="6" class="input">
            <el-form-item prop="input_customer_name">
              <el-input placeholder="专线用户名" clearable size="small" v-model="formFilter.input_customer_name" @keyup.enter.native="DataFilter()"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="6" class="input">
            <el-form-item prop="input_line_code">
              <el-input placeholder="专线号" clearable size="small" v-model="formFilter.input_line_code" @keyup.enter.native="DataFilter()"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="6" class="input">
            <el-form-item prop="input_ipaddress">
              <el-input placeholder="IP地址" clearable size="small" v-model="formFilter.input_ipaddress" @keyup.enter.native="DataFilter()"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="1.5">
            <el-form-item>
              <el-button type="primary" icon="el-icon-search" size="small" @click="DataFilter()">查询</el-button>
            </el-form-item>
          </el-col>
          <el-col :span="1.5">
            <el-form-item>
              <el-button type="success" @click="addCustomer()" size="small">
                <icon name="add" scale="1.5" style="margin-top:-2px; float:left; padding-top:1px; padding-right:5px" ></icon>新增
              </el-button>
            </el-form-item>
          </el-col>
          <el-col :span="1.5">
            <el-form-item>
              <el-button size="small" @click="dialogFormUploadVisible = true">
                <icon name="upload" scale="1.5" style="margin-top:-2px; float:left; padding-top:1px; padding-right:5px"></icon>批量导入</el-button>
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
      <el-table-column prop="organization" label="组织" align="center"  width="80">
      </el-table-column>
      <el-table-column prop="src_address" label="起始地址" align="center">
      </el-table-column>
      <el-table-column prop="dst_address" label="结束地址" align="center">
      </el-table-column>
<!--       <el-table-column prop="mode" label="使用方式" align="center" width="80">
      </el-table-column> -->
      <el-table-column prop="customer_name" label="用户名称" align="center">
      </el-table-column>
      <el-table-column prop="customer_address" label="用户地址" align="center">
      </el-table-column>
      <el-table-column prop="customer_type" label="用户类型" align="center" width="100">
      </el-table-column>
      <el-table-column prop="line_code" label="专线号" align="center">
      </el-table-column>
      <el-table-column label="操作" align="center">
        <template slot-scope="scope">
          <el-button size="mini" type="text" @click="handleEdit(scope.$index, scope.row)">
            <icon name="edit" scale="1.5" style="margin-top:-2px; float:left; padding-top:1px"></icon>编辑</el-button>
          <el-button size="mini" type="text" @click="handleDelete(scope.row)">
            <icon name="del" scale="1.5" style="margin-top:-2px; float:left; padding-top:1px"></icon><span>删除</span></el-button>
        </template>
      </el-table-column>
    </el-table>


    <!-- 编辑Form -->
    <el-dialog title="编辑客户信息" :visible.sync="dialogFormEditVisible">
      <el-form :model="formEdit" :rules="formEditRules" ref="formEdit">
        <el-row>
        <el-col :span="12">
          <el-form-item label="组织" :label-width="formLabelWidth" size="small" prop="organization">
            <el-input v-model="formEdit.organization" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="用户名称" :label-width="formLabelWidth" size="small" prop="customer_name">
            <el-input v-model="formEdit.customer_name" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="起始地址" :label-width="formLabelWidth" size="small" prop="src_address">
            <el-input v-model="formEdit.src_address" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="结束地址" :label-width="formLabelWidth" size="small" prop="dst_address">
            <el-input v-model="formEdit.dst_address" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="24">
          <el-form-item label="用户地址" :label-width="formLabelWidth" size="small" prop="customer_address">
            <el-input v-model="formEdit.customer_address" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="专线类型" prop="customer_type">
            <el-select v-model="formEdit.customer_type" size="small" style="width: calc(100% - 80px)">
              <el-option label="专线（SR）" value="专线（SR）"></el-option>
              <el-option label="专线（BAS）" value="专线（BAS）"></el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="专线号" :label-width="formLabelWidth" size="small" prop="line_code">
            <el-input v-model="formEdit.line_code" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        </el-row>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormEditVisible=false" size="small">取 消</el-button>
        <el-button type="primary" @click="submitFormEdit()" size="small">确 定</el-button>
      </div>
    </el-dialog>

    <!-- 新增Form -->
    <el-dialog title="新增客户信息" :visible.sync="dialogFormAddVisible">
      <el-form ref="formAdd" :model="formAdd" :rules="formAddRules">
        <el-row>
        <el-col :span="12">
          <el-form-item label="组织" :label-width="formLabelWidth" size="small" prop="organization">
            <el-input v-model="formAdd.organization" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="用户名称" :label-width="formLabelWidth" size="small" prop="customer_name">
            <el-input v-model="formAdd.customer_name" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="起始地址" :label-width="formLabelWidth" size="small" prop="src_address">
            <el-input v-model="formAdd.src_address" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="结束地址" :label-width="formLabelWidth" size="small" prop="dst_address">
            <el-input v-model="formAdd.dst_address" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="24">
          <el-form-item label="用户地址" :label-width="formLabelWidth" size="small" prop="customer_address">
            <el-input v-model="formAdd.customer_address" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="专线类型" :label-width="formLabelWidth" size="small" prop="customer_type">
            <el-select v-model="formAdd.customer_type" size="small" style="width: 100%">
              <el-option label="专线（SR）" value="专线（SR）"></el-option>
              <el-option label="专线（BAS）" value="专线（BAS）"></el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="专线号" :label-width="formLabelWidth" size="small" prop="line_code">
            <el-input v-model="formAdd.line_code" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        </el-row>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="cancelFormAdd()" size="small">取 消</el-button>
        <el-button type="primary" @click="submitFormAdd()" size="small">确 定</el-button>
      </div>
    </el-dialog>
    
    <div style="text-align:center">
      <el-dialog title="导入" :visible.sync="dialogFormUploadVisible">
        <el-upload
          ref="upload"
          :action="uploadDataUrl"
          :multiple="false"
          :limit="1"
          :file-list="fileList"
          :on-success="successUpload"
          :auto-upload="false">
          <el-button slot="trigger" size="small" type="primary" @click="clearUploaded" >选取文件</el-button>
          <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传</el-button>
          <div slot="tip" class="el-upload__tip">只能上传xlsx文件</div>
        </el-upload>
      </el-dialog>
    </div>
    
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

  function isValidIP(ip) {
    var reg =  /(^0|([1-9]\d{0,1})|1\d\d|2[0-4]\d|25[0-5])\.(0|([1-9]\d{0,1})|1\d\d|2[0-4]\d|25[0-5])\.(0|([1-9]\d{0,1})|1\d\d|2[0-4]\d|25[0-5])\.(0|([1-9]\d{0,1})|1\d\d|2[0-4]\d|25[0-5])$/;
    return reg.test(ip);
  }
  export default {
    data() {
      var ipAddressValidator = (rule, value, callback) => {
        if(!value){ return callback(new Error('IP地址不能为空')); }
        setTimeout(() => {
          if(!isValidIP(value)){
            callback(new Error("IP地址不符合要求"));
          } else { callback(); }
        }, 100);
      };
      return {
        data: [],
        currentPage:1,
        pageSize:10,
        formLabelWidth: '80px',
        dialogFormEditVisible: false,
        dialogFormAddVisible: false,
        dialogFormUploadVisible: false,
        formFilter: {
          input_customer_name: '',
          input_line_code: '',
          input_ipaddress: ''
        },
        formEdit: {
          organization: '',
          src_address: '',
          dst_address: '',
          customer_name: '',
          customer_address: '',
          customer_type: '',
          line_code: ''
        },
        formAdd: {
          organization: '',
          src_address: '',
          dst_address: '',
          customer_name: '',
          customer_address: '',
          customer_type: '',
          line_code: ''
        },
        formEditRules: {
          organization:[{
            required: true,
            message: '请输入组织',
            trigger: 'blur'
          }],
          src_address:[{
            required: true,
            validator: ipAddressValidator,
            trigger: 'blur'
          }],
          dst_address:[{
            required: true,
            validator: ipAddressValidator,
            trigger: 'blur'
          }],
          customer_name:[{
            required: true,
            message: '请输入客户名称',
            trigger: 'blur'
          }],
          customer_address:[{
            required: true,
            message: '请输入客户地址',
            trigger: 'blur'
          }],
          customer_type:[{
            required: true,
            message: '请输入专线类型',
            trigger: 'blur'
          }],
          line_code:[{
            required: true,
            message: '请输入专线号',
            trigger: 'blur'
          }]
        },
        formAddRules: {
          organization:[{
            required: true,
            message: '请输入组织',
            trigger: 'blur'
          }],
          src_address:[{
            required: true,
            validator: ipAddressValidator,
            trigger: 'blur'
          }],
          dst_address:[{
            required: true,
            validator: ipAddressValidator,
            trigger: 'blur'
          }],
          customer_name:[{
            required: true,
            message: '请输入客户名称',
            trigger: 'blur'
          }],
          customer_address:[{
            required: true,
            message: '请输入客户地址',
            trigger: 'blur'
          }],
          customer_type:[{
            required: true,
            message: '请输入专线类型',
            trigger: 'blur'
          }],
          line_code:[{
            required: true,
            message: '请输入专线号',
            trigger: 'blur'
          }]
        }
      }
    },
    methods: {

      handleSizeChange(size) {
       this.pageSize = size;
      },

      handleCurrentChange(currentPage) {
        this.currentPage = currentPage;
      },

      DataFilter() {
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-customer-info',
          data: {
            'customer_name': this.formFilter.input_customer_name,
            'ipaddress': this.formFilter.input_ipaddress,
            'line_code': this.formFilter.input_line_code
          }
        }).then(response => {
          if(response.data.status){
            this.data = response.data.data;
          }
        }).catch(error => {});
      },

      addCustomer(){
        this.dialogFormAddVisible = true;
        //this.$refs.formAdd.resetFields();
      },

      cancelFormAdd(){
        this.dialogFormAddVisible = false;
        this.$refs.formAdd.resetFields();
      },
    
      handleEdit(index, row) {
        this.dialogFormEditVisible = true;
        this.formEdit = Object.assign({}, row);
      },

      handleDelete(row) {
        this.$confirm('是否将该记录删除?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$http({
            method: 'post',
            url: restful_path + '/api/dns/delete-customer-info',
            data: {
              'id': row['id']
            }
          }).then((response) => {
            if(response.data.msg){
              this.$message({
                type: 'success',
                message: '删除成功!'
              });
              setTimeout(() =>{
                this.$http({
                  method: 'post',
                  url: restful_path + '/api/dns/get-customer-info',
                  data: {
                    'customer_name': '',
                    'ipaddress': '',
                    'line_code': ''
                  }
                  }).then(response => {
                    if(response.data.msg) {
                      this.data = response.data.data
                    }
                  })
                  .catch(error => {})
              }, 100)
            }
          }).catch(error => {});
        }).catch(() => {});
      },

      submitFormAdd() {
        this.$refs.formAdd.validate((valid) => {
          if(valid){
            this.$http({
              method: 'post',
              url: restful_path + '/api/dns/customer-info/add',
              data: {
                'organization': this.formAdd.organization,
                'customer_name': this.formAdd.customer_name,
                'src_address': this.formAdd.src_address,
                'dst_address': this.formAdd.dst_address,
                'customer_name': this.formAdd.customer_name,
                'customer_address': this.formAdd.customer_address,
                'customer_type': this.formAdd.customer_type,
                'line_code': this.formAdd.line_code
              }
            }).then(response => {
              //this.buttonDisabled = false;
              if (response.data.status){
                this.$message({ type: 'success', message: '添加客户信息成功!' });
              } else {
                this.$message({ type: 'error', message: '添加客户信息失败!' });
              }
              this.$refs.formAdd.resetFields();
              //this.default_keys = [];
              this.dialogFormAddVisible = false;
              setTimeout(() => { this.DataFilter() }, 100);
            }).catch(error => {
              //console.log(error);
            });
          }
        })
      },

      submitFormEdit() {
        this.$refs.formEdit.validate((valid) => { if(valid) {
          let para = Object.assign({}, this.formEdit);
          this.$http({
              method: 'post',
              url: restful_path + '/api/dns/customer-info/edit/' + para.id,
              data: {
                'organization': para.organization,
                'customer_name': para.customer_name,
                'src_address': para.src_address,
                'dst_address': para.dst_address,
                'customer_name': para.customer_name,
                'customer_address': para.customer_address,
                'customer_type': para.customer_type,
                'line_code': para.line_code,
              }
            }).then(response => { 
              if(response.data.msg) {
                this.$message({
                  type: 'success',
                  message: '修改成功!'
                });
              } else {
                this.$message({
                  type: 'danger',
                  message: '修改失败!'
                });
              }
             }).catch(error => {
              console.log(error);
            });
            this.dialogFormEditVisible = false;
            this.$refs.formEdit.resetFields();
            setTimeout(() =>{
              this.$http({
                method: 'post',
                url: restful_path + '/api/dns/get-customer-info',
                data: {
                  'customer_name': this.formFilter.input_customer_name,
                  'ipaddress': this.formFilter.input_ipaddress,
                  'line_code': this.formFilter.input_line_code
                }
                }).then(response => {
                  this.data = response.data.data
                })
                .catch(error => {
                  console.log(error);
                })
            }, 100)
          }
        });
      },

      submitUpload() {
        this.$refs.upload.submit();
      },
      clearUploaded(){
        this.$refs.upload.clearFiles();
      },

      
    }
  }
</script>

<style lang="scss" scoped>
  .handle-box{
    margin-top: 20px;
    text-align: center;
  }
  .handle-input{
    width: 300px;
  }

  .el-input__inner {
    margin-right: 10px;
  }
  .input {
    width:200px;
  }
</style>
