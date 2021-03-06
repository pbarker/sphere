// Code generated by protoc-gen-go. DO NOT EDIT.
// source: v1alpha/sphere.proto

package spherev1alpha

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	timestamp "github.com/golang/protobuf/ptypes/timestamp"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

// Request to register a server.
type RegisterServerRequest struct {
	// Server to register.
	Server               *Server  `protobuf:"bytes,1,opt,name=server,proto3" json:"server,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *RegisterServerRequest) Reset()         { *m = RegisterServerRequest{} }
func (m *RegisterServerRequest) String() string { return proto.CompactTextString(m) }
func (*RegisterServerRequest) ProtoMessage()    {}
func (*RegisterServerRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_24a3247445db88ed, []int{0}
}

func (m *RegisterServerRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_RegisterServerRequest.Unmarshal(m, b)
}
func (m *RegisterServerRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_RegisterServerRequest.Marshal(b, m, deterministic)
}
func (m *RegisterServerRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_RegisterServerRequest.Merge(m, src)
}
func (m *RegisterServerRequest) XXX_Size() int {
	return xxx_messageInfo_RegisterServerRequest.Size(m)
}
func (m *RegisterServerRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_RegisterServerRequest.DiscardUnknown(m)
}

var xxx_messageInfo_RegisterServerRequest proto.InternalMessageInfo

func (m *RegisterServerRequest) GetServer() *Server {
	if m != nil {
		return m.Server
	}
	return nil
}

// Response from registering a server.
type RegisterServerResponse struct {
	// Server registered.
	Server               *Server  `protobuf:"bytes,1,opt,name=server,proto3" json:"server,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *RegisterServerResponse) Reset()         { *m = RegisterServerResponse{} }
func (m *RegisterServerResponse) String() string { return proto.CompactTextString(m) }
func (*RegisterServerResponse) ProtoMessage()    {}
func (*RegisterServerResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_24a3247445db88ed, []int{1}
}

func (m *RegisterServerResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_RegisterServerResponse.Unmarshal(m, b)
}
func (m *RegisterServerResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_RegisterServerResponse.Marshal(b, m, deterministic)
}
func (m *RegisterServerResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_RegisterServerResponse.Merge(m, src)
}
func (m *RegisterServerResponse) XXX_Size() int {
	return xxx_messageInfo_RegisterServerResponse.Size(m)
}
func (m *RegisterServerResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_RegisterServerResponse.DiscardUnknown(m)
}

var xxx_messageInfo_RegisterServerResponse proto.InternalMessageInfo

func (m *RegisterServerResponse) GetServer() *Server {
	if m != nil {
		return m.Server
	}
	return nil
}

// Request to get a server.
type GetServerRequest struct {
	// ID of the server.
	Id                   string   `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *GetServerRequest) Reset()         { *m = GetServerRequest{} }
func (m *GetServerRequest) String() string { return proto.CompactTextString(m) }
func (*GetServerRequest) ProtoMessage()    {}
func (*GetServerRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_24a3247445db88ed, []int{2}
}

func (m *GetServerRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_GetServerRequest.Unmarshal(m, b)
}
func (m *GetServerRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_GetServerRequest.Marshal(b, m, deterministic)
}
func (m *GetServerRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GetServerRequest.Merge(m, src)
}
func (m *GetServerRequest) XXX_Size() int {
	return xxx_messageInfo_GetServerRequest.Size(m)
}
func (m *GetServerRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_GetServerRequest.DiscardUnknown(m)
}

var xxx_messageInfo_GetServerRequest proto.InternalMessageInfo

func (m *GetServerRequest) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

// Response from getting a server.
type GetServerResponse struct {
	// Server retrieved.
	Server               *Server  `protobuf:"bytes,1,opt,name=server,proto3" json:"server,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *GetServerResponse) Reset()         { *m = GetServerResponse{} }
func (m *GetServerResponse) String() string { return proto.CompactTextString(m) }
func (*GetServerResponse) ProtoMessage()    {}
func (*GetServerResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_24a3247445db88ed, []int{3}
}

func (m *GetServerResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_GetServerResponse.Unmarshal(m, b)
}
func (m *GetServerResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_GetServerResponse.Marshal(b, m, deterministic)
}
func (m *GetServerResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GetServerResponse.Merge(m, src)
}
func (m *GetServerResponse) XXX_Size() int {
	return xxx_messageInfo_GetServerResponse.Size(m)
}
func (m *GetServerResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_GetServerResponse.DiscardUnknown(m)
}

var xxx_messageInfo_GetServerResponse proto.InternalMessageInfo

func (m *GetServerResponse) GetServer() *Server {
	if m != nil {
		return m.Server
	}
	return nil
}

// Request to list servers.
type ListServerRequest struct {
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ListServerRequest) Reset()         { *m = ListServerRequest{} }
func (m *ListServerRequest) String() string { return proto.CompactTextString(m) }
func (*ListServerRequest) ProtoMessage()    {}
func (*ListServerRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_24a3247445db88ed, []int{4}
}

func (m *ListServerRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ListServerRequest.Unmarshal(m, b)
}
func (m *ListServerRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ListServerRequest.Marshal(b, m, deterministic)
}
func (m *ListServerRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ListServerRequest.Merge(m, src)
}
func (m *ListServerRequest) XXX_Size() int {
	return xxx_messageInfo_ListServerRequest.Size(m)
}
func (m *ListServerRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_ListServerRequest.DiscardUnknown(m)
}

var xxx_messageInfo_ListServerRequest proto.InternalMessageInfo

// Response from listing servers.
type ListServerResponse struct {
	// Servers from listing.
	Servers              []*Server `protobuf:"bytes,1,rep,name=servers,proto3" json:"servers,omitempty"`
	XXX_NoUnkeyedLiteral struct{}  `json:"-"`
	XXX_unrecognized     []byte    `json:"-"`
	XXX_sizecache        int32     `json:"-"`
}

func (m *ListServerResponse) Reset()         { *m = ListServerResponse{} }
func (m *ListServerResponse) String() string { return proto.CompactTextString(m) }
func (*ListServerResponse) ProtoMessage()    {}
func (*ListServerResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_24a3247445db88ed, []int{5}
}

func (m *ListServerResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ListServerResponse.Unmarshal(m, b)
}
func (m *ListServerResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ListServerResponse.Marshal(b, m, deterministic)
}
func (m *ListServerResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ListServerResponse.Merge(m, src)
}
func (m *ListServerResponse) XXX_Size() int {
	return xxx_messageInfo_ListServerResponse.Size(m)
}
func (m *ListServerResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_ListServerResponse.DiscardUnknown(m)
}

var xxx_messageInfo_ListServerResponse proto.InternalMessageInfo

func (m *ListServerResponse) GetServers() []*Server {
	if m != nil {
		return m.Servers
	}
	return nil
}

// Request to unregister a server.
type UnregisterServerRequest struct {
	// ID of the server.
	Id                   string   `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *UnregisterServerRequest) Reset()         { *m = UnregisterServerRequest{} }
func (m *UnregisterServerRequest) String() string { return proto.CompactTextString(m) }
func (*UnregisterServerRequest) ProtoMessage()    {}
func (*UnregisterServerRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_24a3247445db88ed, []int{6}
}

func (m *UnregisterServerRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_UnregisterServerRequest.Unmarshal(m, b)
}
func (m *UnregisterServerRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_UnregisterServerRequest.Marshal(b, m, deterministic)
}
func (m *UnregisterServerRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_UnregisterServerRequest.Merge(m, src)
}
func (m *UnregisterServerRequest) XXX_Size() int {
	return xxx_messageInfo_UnregisterServerRequest.Size(m)
}
func (m *UnregisterServerRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_UnregisterServerRequest.DiscardUnknown(m)
}

var xxx_messageInfo_UnregisterServerRequest proto.InternalMessageInfo

func (m *UnregisterServerRequest) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

// Response from unregister a server.
type UnregisterServerResponse struct {
	// Message from unregistering a server.
	Message              string   `protobuf:"bytes,1,opt,name=message,proto3" json:"message,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *UnregisterServerResponse) Reset()         { *m = UnregisterServerResponse{} }
func (m *UnregisterServerResponse) String() string { return proto.CompactTextString(m) }
func (*UnregisterServerResponse) ProtoMessage()    {}
func (*UnregisterServerResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_24a3247445db88ed, []int{7}
}

func (m *UnregisterServerResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_UnregisterServerResponse.Unmarshal(m, b)
}
func (m *UnregisterServerResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_UnregisterServerResponse.Marshal(b, m, deterministic)
}
func (m *UnregisterServerResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_UnregisterServerResponse.Merge(m, src)
}
func (m *UnregisterServerResponse) XXX_Size() int {
	return xxx_messageInfo_UnregisterServerResponse.Size(m)
}
func (m *UnregisterServerResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_UnregisterServerResponse.DiscardUnknown(m)
}

var xxx_messageInfo_UnregisterServerResponse proto.InternalMessageInfo

func (m *UnregisterServerResponse) GetMessage() string {
	if m != nil {
		return m.Message
	}
	return ""
}

// An environment server.
type Server struct {
	// Name of the server.
	Name string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	// Address of the server.
	Address string `protobuf:"bytes,2,opt,name=address,proto3" json:"address,omitempty"`
	// Description of the server.
	Description string `protobuf:"bytes,3,opt,name=description,proto3" json:"description,omitempty"`
	// Time when the server was created.
	CreatedTime *timestamp.Timestamp `protobuf:"bytes,4,opt,name=created_time,json=createdTime,proto3" json:"created_time,omitempty"`
	// ID of the server.
	Id                   string   `protobuf:"bytes,5,opt,name=id,proto3" json:"id,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Server) Reset()         { *m = Server{} }
func (m *Server) String() string { return proto.CompactTextString(m) }
func (*Server) ProtoMessage()    {}
func (*Server) Descriptor() ([]byte, []int) {
	return fileDescriptor_24a3247445db88ed, []int{8}
}

func (m *Server) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Server.Unmarshal(m, b)
}
func (m *Server) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Server.Marshal(b, m, deterministic)
}
func (m *Server) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Server.Merge(m, src)
}
func (m *Server) XXX_Size() int {
	return xxx_messageInfo_Server.Size(m)
}
func (m *Server) XXX_DiscardUnknown() {
	xxx_messageInfo_Server.DiscardUnknown(m)
}

var xxx_messageInfo_Server proto.InternalMessageInfo

func (m *Server) GetName() string {
	if m != nil {
		return m.Name
	}
	return ""
}

func (m *Server) GetAddress() string {
	if m != nil {
		return m.Address
	}
	return ""
}

func (m *Server) GetDescription() string {
	if m != nil {
		return m.Description
	}
	return ""
}

func (m *Server) GetCreatedTime() *timestamp.Timestamp {
	if m != nil {
		return m.CreatedTime
	}
	return nil
}

func (m *Server) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func init() {
	proto.RegisterType((*RegisterServerRequest)(nil), "sphere.api.v1alpha.RegisterServerRequest")
	proto.RegisterType((*RegisterServerResponse)(nil), "sphere.api.v1alpha.RegisterServerResponse")
	proto.RegisterType((*GetServerRequest)(nil), "sphere.api.v1alpha.GetServerRequest")
	proto.RegisterType((*GetServerResponse)(nil), "sphere.api.v1alpha.GetServerResponse")
	proto.RegisterType((*ListServerRequest)(nil), "sphere.api.v1alpha.ListServerRequest")
	proto.RegisterType((*ListServerResponse)(nil), "sphere.api.v1alpha.ListServerResponse")
	proto.RegisterType((*UnregisterServerRequest)(nil), "sphere.api.v1alpha.UnregisterServerRequest")
	proto.RegisterType((*UnregisterServerResponse)(nil), "sphere.api.v1alpha.UnregisterServerResponse")
	proto.RegisterType((*Server)(nil), "sphere.api.v1alpha.Server")
}

func init() { proto.RegisterFile("v1alpha/sphere.proto", fileDescriptor_24a3247445db88ed) }

var fileDescriptor_24a3247445db88ed = []byte{
	// 482 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xa4, 0x93, 0xc1, 0x6e, 0xd3, 0x40,
	0x10, 0x86, 0xe5, 0x34, 0xa4, 0xca, 0x04, 0x4a, 0x3a, 0x10, 0x6a, 0x19, 0x10, 0xd1, 0x0a, 0x10,
	0x0d, 0xc8, 0x16, 0xa1, 0x27, 0x24, 0x0e, 0x70, 0xa9, 0x80, 0x1e, 0x50, 0x0a, 0x17, 0x2e, 0x68,
	0x5b, 0x0f, 0xe9, 0x4a, 0x8d, 0x6d, 0x76, 0xb6, 0xe1, 0x80, 0xb8, 0x20, 0x8e, 0x9c, 0xe0, 0x21,
	0x78, 0x20, 0x5e, 0x81, 0x07, 0x41, 0xd9, 0x5d, 0x97, 0xc4, 0x31, 0x4a, 0x45, 0x6f, 0x99, 0xd9,
	0x7f, 0xfe, 0x3f, 0x33, 0xf9, 0x02, 0x57, 0xa7, 0x0f, 0xe5, 0x71, 0x71, 0x24, 0x13, 0x2e, 0x8e,
	0x48, 0x53, 0x5c, 0xe8, 0xdc, 0xe4, 0x88, 0xbe, 0x92, 0x85, 0x8a, 0xbd, 0x20, 0xba, 0x31, 0xce,
	0xf3, 0xf1, 0x31, 0x25, 0xb2, 0x50, 0x89, 0xcc, 0xb2, 0xdc, 0x48, 0xa3, 0xf2, 0x8c, 0xdd, 0x44,
	0x74, 0xcb, 0xbf, 0xda, 0xea, 0xe0, 0xe4, 0x7d, 0x62, 0xd4, 0x84, 0xd8, 0xc8, 0x49, 0xe1, 0x04,
	0xe2, 0x25, 0xf4, 0x46, 0x34, 0x56, 0x6c, 0x48, 0xef, 0x93, 0x9e, 0x92, 0x1e, 0xd1, 0x87, 0x13,
	0x62, 0x83, 0x43, 0x68, 0xb1, 0x6d, 0x84, 0x41, 0x3f, 0xb8, 0xd7, 0x19, 0x46, 0xf1, 0x72, 0x78,
	0xec, 0x47, 0xbc, 0x52, 0xec, 0xc1, 0xb5, 0xaa, 0x19, 0x17, 0x79, 0xc6, 0xf4, 0x5f, 0x6e, 0x02,
	0xba, 0xbb, 0x64, 0x16, 0xbf, 0xd5, 0x06, 0x34, 0x54, 0x6a, 0x3d, 0xda, 0xa3, 0x86, 0x4a, 0xc5,
	0x2e, 0x6c, 0xce, 0x69, 0xce, 0x11, 0x76, 0x05, 0x36, 0xf7, 0x14, 0x2f, 0xa6, 0x89, 0x17, 0x80,
	0xf3, 0x4d, 0x6f, 0xbf, 0x03, 0xeb, 0x6e, 0x88, 0xc3, 0xa0, 0xbf, 0xb6, 0xc2, 0xbf, 0x94, 0x8a,
	0x6d, 0xd8, 0x7a, 0x93, 0xe9, 0xda, 0x53, 0x57, 0x97, 0xda, 0x81, 0x70, 0x59, 0xea, 0xc3, 0x43,
	0x58, 0x9f, 0x10, 0xb3, 0x1c, 0x93, 0x1f, 0x28, 0x4b, 0xf1, 0x33, 0x80, 0x96, 0x13, 0x23, 0x42,
	0x33, 0x93, 0x93, 0x52, 0x61, 0x3f, 0xcf, 0x06, 0x65, 0x9a, 0x6a, 0x62, 0x0e, 0x1b, 0x6e, 0xd0,
	0x97, 0xd8, 0x87, 0x4e, 0x4a, 0x7c, 0xa8, 0x55, 0x31, 0x23, 0x27, 0x5c, 0xb3, 0xaf, 0xf3, 0x2d,
	0x7c, 0x02, 0x17, 0x0f, 0x35, 0x49, 0x43, 0xe9, 0xbb, 0x19, 0x3f, 0x61, 0xd3, 0x9f, 0xd5, 0xc1,
	0x15, 0x97, 0x70, 0xc5, 0xaf, 0x4b, 0xb8, 0x46, 0x1d, 0xaf, 0x9f, 0x75, 0xfc, 0x7e, 0x17, 0xca,
	0xfd, 0x86, 0xdf, 0x9b, 0xd0, 0xde, 0xb7, 0x17, 0x7b, 0xfa, 0xea, 0x39, 0x7e, 0x0d, 0x60, 0x63,
	0x91, 0x1a, 0xdc, 0xae, 0x3b, 0x68, 0x2d, 0xa6, 0xd1, 0xe0, 0x2c, 0x52, 0x77, 0x3b, 0x71, 0xfd,
	0xcb, 0xaf, 0xdf, 0x3f, 0x1a, 0x3d, 0xd1, 0x4d, 0x4e, 0xff, 0x5d, 0xee, 0xc7, 0x79, 0x1c, 0x0c,
	0xf0, 0x23, 0xb4, 0x4f, 0x49, 0xc2, 0xdb, 0x75, 0xae, 0x55, 0x18, 0xa3, 0x3b, 0x2b, 0x54, 0x3e,
	0xf6, 0xa6, 0x8d, 0xdd, 0xc2, 0x5e, 0x35, 0x36, 0xf9, 0xa4, 0xd2, 0xcf, 0x38, 0x85, 0xce, 0x5f,
	0xc8, 0x18, 0x6b, 0x4d, 0x97, 0xd0, 0x8c, 0xee, 0xae, 0x92, 0xf9, 0xf0, 0xd0, 0x86, 0x23, 0x2e,
	0xed, 0x8c, 0xdf, 0x02, 0xe8, 0x56, 0x31, 0xc3, 0xfb, 0x75, 0xb6, 0xff, 0xe0, 0x36, 0x7a, 0x70,
	0x36, 0xf1, 0xe2, 0x19, 0x06, 0xf5, 0x67, 0x78, 0x76, 0xf9, 0xed, 0x25, 0xe7, 0xe6, 0x5f, 0x0f,
	0x5a, 0x16, 0xab, 0x47, 0x7f, 0x02, 0x00, 0x00, 0xff, 0xff, 0x4f, 0xe8, 0x35, 0x82, 0x0b, 0x05,
	0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// SphereAPIClient is the client API for SphereAPI service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type SphereAPIClient interface {
	// Register an environment server.
	RegisterServer(ctx context.Context, in *RegisterServerRequest, opts ...grpc.CallOption) (*RegisterServerResponse, error)
	// Get environment server.
	GetServer(ctx context.Context, in *GetServerRequest, opts ...grpc.CallOption) (*GetServerResponse, error)
	// List environment servers.
	ListServers(ctx context.Context, in *ListServerRequest, opts ...grpc.CallOption) (*ListServerResponse, error)
	// Unregister environment server.
	UnregisterServer(ctx context.Context, in *UnregisterServerRequest, opts ...grpc.CallOption) (*UnregisterServerResponse, error)
}

type sphereAPIClient struct {
	cc *grpc.ClientConn
}

func NewSphereAPIClient(cc *grpc.ClientConn) SphereAPIClient {
	return &sphereAPIClient{cc}
}

func (c *sphereAPIClient) RegisterServer(ctx context.Context, in *RegisterServerRequest, opts ...grpc.CallOption) (*RegisterServerResponse, error) {
	out := new(RegisterServerResponse)
	err := c.cc.Invoke(ctx, "/sphere.api.v1alpha.SphereAPI/RegisterServer", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sphereAPIClient) GetServer(ctx context.Context, in *GetServerRequest, opts ...grpc.CallOption) (*GetServerResponse, error) {
	out := new(GetServerResponse)
	err := c.cc.Invoke(ctx, "/sphere.api.v1alpha.SphereAPI/GetServer", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sphereAPIClient) ListServers(ctx context.Context, in *ListServerRequest, opts ...grpc.CallOption) (*ListServerResponse, error) {
	out := new(ListServerResponse)
	err := c.cc.Invoke(ctx, "/sphere.api.v1alpha.SphereAPI/ListServers", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sphereAPIClient) UnregisterServer(ctx context.Context, in *UnregisterServerRequest, opts ...grpc.CallOption) (*UnregisterServerResponse, error) {
	out := new(UnregisterServerResponse)
	err := c.cc.Invoke(ctx, "/sphere.api.v1alpha.SphereAPI/UnregisterServer", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SphereAPIServer is the server API for SphereAPI service.
type SphereAPIServer interface {
	// Register an environment server.
	RegisterServer(context.Context, *RegisterServerRequest) (*RegisterServerResponse, error)
	// Get environment server.
	GetServer(context.Context, *GetServerRequest) (*GetServerResponse, error)
	// List environment servers.
	ListServers(context.Context, *ListServerRequest) (*ListServerResponse, error)
	// Unregister environment server.
	UnregisterServer(context.Context, *UnregisterServerRequest) (*UnregisterServerResponse, error)
}

// UnimplementedSphereAPIServer can be embedded to have forward compatible implementations.
type UnimplementedSphereAPIServer struct {
}

func (*UnimplementedSphereAPIServer) RegisterServer(ctx context.Context, req *RegisterServerRequest) (*RegisterServerResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RegisterServer not implemented")
}
func (*UnimplementedSphereAPIServer) GetServer(ctx context.Context, req *GetServerRequest) (*GetServerResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetServer not implemented")
}
func (*UnimplementedSphereAPIServer) ListServers(ctx context.Context, req *ListServerRequest) (*ListServerResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListServers not implemented")
}
func (*UnimplementedSphereAPIServer) UnregisterServer(ctx context.Context, req *UnregisterServerRequest) (*UnregisterServerResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UnregisterServer not implemented")
}

func RegisterSphereAPIServer(s *grpc.Server, srv SphereAPIServer) {
	s.RegisterService(&_SphereAPI_serviceDesc, srv)
}

func _SphereAPI_RegisterServer_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(RegisterServerRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SphereAPIServer).RegisterServer(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/sphere.api.v1alpha.SphereAPI/RegisterServer",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SphereAPIServer).RegisterServer(ctx, req.(*RegisterServerRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SphereAPI_GetServer_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetServerRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SphereAPIServer).GetServer(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/sphere.api.v1alpha.SphereAPI/GetServer",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SphereAPIServer).GetServer(ctx, req.(*GetServerRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SphereAPI_ListServers_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListServerRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SphereAPIServer).ListServers(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/sphere.api.v1alpha.SphereAPI/ListServers",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SphereAPIServer).ListServers(ctx, req.(*ListServerRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SphereAPI_UnregisterServer_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UnregisterServerRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SphereAPIServer).UnregisterServer(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/sphere.api.v1alpha.SphereAPI/UnregisterServer",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SphereAPIServer).UnregisterServer(ctx, req.(*UnregisterServerRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _SphereAPI_serviceDesc = grpc.ServiceDesc{
	ServiceName: "sphere.api.v1alpha.SphereAPI",
	HandlerType: (*SphereAPIServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "RegisterServer",
			Handler:    _SphereAPI_RegisterServer_Handler,
		},
		{
			MethodName: "GetServer",
			Handler:    _SphereAPI_GetServer_Handler,
		},
		{
			MethodName: "ListServers",
			Handler:    _SphereAPI_ListServers_Handler,
		},
		{
			MethodName: "UnregisterServer",
			Handler:    _SphereAPI_UnregisterServer_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "v1alpha/sphere.proto",
}
